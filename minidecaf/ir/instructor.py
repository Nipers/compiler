from ..utils import *
#中间码种类，目前有Ret和Const
class IRInstr:
    def __repr__(self):
        return self.__str__()

class Ret(IRInstr):
    def __str__(self):
        return f"ret"
    
    def accept(self, visitor):
        visitor.visitRet(self)

class Const(IRInstr):#曾经试图改过这个指令的名字，但目前暂时和指导书保持一致
    def __init__(self, value:int):
        assert MIN_INT <= value <= MAX_INT
        self.value = value
    def __str__(self):
        return f"Const {self.value}"
        

class Unary(IRInstr):#一元运算
    def __init__(self, op:str):
        assert op in unaryOps
        self.op = op

    def __str__(self):
        return strOfUnaryOp[self.op]
   

class Binary(IRInstr):#二元运算
    def __init__(self, op:str):
        assert op in binaryOps
        self.op = op
    
    def __str__(self):
        return strOfBinaryOp[self.op]


class Pop(IRInstr):
    def __str__(self):
        return f"pop"

class Load(IRInstr):
    def __str__(self):
        return f"load"

class FrameSlot(IRInstr):
    def __init__(self, offset:int):
        assert offset < 0
        self.offset = offset

    def __str__(self):
        return f"frameslot {self.offset}"

    def accept(self, visitor):
        visitor.visitFrameSlot(self)
        
class Store:
    def __str__(self):
        return f"store"

class Comment(IRInstr):
    def __init__(self, content:str):
        self.content = content
    
    def __str__(self):
        return f"# {self.content}"

class Label(IRInstr):
    def __init__(self, label:str):
        self.label = label

    def __str__(self):
        return f"{self.label}:"

class Branch(IRInstr):
    def __init__(self, op:str, label:str):
        assert op in branchOps
        self.op = op
        self.label = label

    def __str__(self):
        return f"{self.op} {self.label}"

class GlobalSymbol(IRInstr):
    def __init__(self, symbol:str):
        self.symbol = symbol
    
    def __str__(self):
        return f"globalsymbol {self.symbol}"

class FuncCall(IRInstr):
    def __init__(self, funcName:str):
        self.funcName = funcName
    
    def __str__(self):
        return f"call {self.funcName}"
