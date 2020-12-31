from ..utils import *

class Type:
    def __repr__(self):
        return super().__repr__()

    def size(self):
        raise MiniDecafTypeError("abstract type is not allowed")

class Void:
    def __init__(self):
        pass

    def __str__(self):
        return "Void"

    def __eq__(self, value):
        return isinstance(value, Void)


class Int(Type):
    def __init__(self):
        pass

    def __str__(self):
        return "Int"

    def __eq__(self, value):
        return isinstance(value, Int)

    def size(self):
        return INT_BYTES

class Pointer(Type):
    def __init__(self, base:Type):
        self.base = base
    
    def __str__(self):
        return f"{self.base}"

    def __eq__(self, value):
        if not isinstance(value, Pointer):
            return False
        return self.base == value.base

    def size(self):
        return INT_BYTES

class Array(Type):
    def __init__(self, base:Type, length:int):
        self.base = base
        self.length = length

    def __str__(self):
        return f"{self.base}[{self.length}]"

    def __eq__(self, value):
        if not isinstance(value, Array):
            return False
        return self.base == value.base and self.length == value.length

    def size(self):
        return self.base.size() * self.length

def make(base:Type, dims:list):#构造多维数组
    for length in dims:
        base = Array(base, length)
    return base

class Zero(Int, Pointer):
    def __init__(self):
        pass

    def __str__(self):
        return "Zero"

    def __eq__(self, value):
        return isinstance(value, Int) or isinstance(value, Pointer)

def TypeRule(func):
    def g(ctx, *inType):
        result = func(ctx, *inType)
        if type(result) is str:
            raise MiniDecafTypeError(ctx, f"{func.__name__}: {result}")
        if result is None:
            raise MiniDecafTypeError(ctx, f"{func.__name__}: type error")
        return result
    g.__name__ = func.__name__
    return g

def tryAll(name = "tryAll", *funcs):
    @TypeRule
    def g(ctx, *inType):
        errors = []
        for func in  funcs:
            try:
                return func(ctx, *inType)
            except MiniDecafTypeError as e:
                errors += [e.msg]
        return f"{name}:\n\t" + "\n\t".join(map(str, errors))
    g.__name__ = name
    return g

@TypeRule
def condRule(ctx, cond, tr, fal):
    if cond == Int() and tr == fal:
        return tr

@TypeRule
def intBinRule(ctx, lhs, rhs):
    if lhs == Int() and rhs == Int():
        return Int()
    return f"int expected, got {lhs} and {rhs}"

@TypeRule
def intUnaRule(ctx, tp):
    if tp == Int():
        return Int()
    return f"int expected, got {tp}"

@TypeRule
def pointerCalRule(ctx, lhs, rhs):
    if lhs == Int() and isinstance(rhs, Pointer):
        return rhs
    if rhs == Int() and isinstance(lhs, Pointer):
        return lhs
    return f"pointer and int expected, got {lhs} and {rhs}"

@TypeRule
def pointerDiffRule(ctx, lhs, rhs):
    if lhs == rhs and isinstance(rhs, Pointer):
        return Int()
    return f"expect two pointers of the same type, got {lhs} and {rhs}"


@TypeRule
def derefRule(ctx, tp):
    if isinstance(tp, Pointer):
        return tp.base
    return f"expect pointer, got {tp}"

@TypeRule
def addrofRule(ctx, tp):
    if isinstance(tp, Array):
        return "can't take address of an array"
    return Pointer(tp)

@TypeRule
def eqRule(ctx, lhs, rhs):
    if lhs != rhs:
        return f"can't equate or compare {lhs} with {rhs}"
    if lhs != Int() and not isinstance(lhs, Pointer):
        return f"expect int or pointer, got {lhs}"
    return Int()

@TypeRule
def relRule(ctx, lhs, rhs):
    if lhs != Int():
        return f"int expected as lhs, got {lhs}"
    if rhs != Int():
        return f"int expected as rhs, got {rhs}"
    return Int()

@TypeRule
def asgnRule(ctx, lhs, rhs):
    if lhs != rhs:
        return f"can't assign {rhs} to {lhs}"
    if isinstance(lhs, Array):
        return f"can't assign  to array {lhs}"
    return lhs

@TypeRule
def retRule(ctx, RetTp, tp):
    if RetTp != tp:
        return f"expect to return {RetTp}, got {tp}"
    return Void()

@TypeRule
def stmtCondRule(ctx, tp):
    if tp != Int():
        return f"expect int, got {tp}"
    return Void()

@TypeRule
def arrayRule(ctx, array, index):
    if not isinstance(array, Array) and not isinstance(array, Pointer):
        return f"expect array or pointer, got {array}"
    if index != Int():
        return f"index must be an integer, got {index}"
    return array.base


    