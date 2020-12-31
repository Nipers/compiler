import sys
from copy import deepcopy

INT_BYTES = 4

MAX_INT = 2**(INT_BYTES*8-1) - 1
MIN_INT = -MAX_INT - 1

class MiniDecafError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

class MiniDecafLocatedError(MiniDecafError):
    def __init__(self, ctx, msg:str):
        self.msg = msg
        self.locatedMsg = f"input:{ctx.start.line},{ctx.start.column}: {msg}"

    def __str__(self):
        return self.locatedMsg


def safeEval(s:str):
    from ast import literal_eval
    return literal_eval(s)


class MiniDecafTypeError(MiniDecafLocatedError):
    pass

class stacked_dict:#栈结构的字典
    def __init__(self):
        self.s = [{}]
        self.d = [{}]

    def __getitem__(self, key):
        return self.s[-1][key]

    def __setitem__(self, key, value):
        self.d[-1][key] = self.s[-1][key] = value

    def __contains__(self, key):
        return key in self.s[-1]

    def __len__(self):
        return len(self.s[-1])

    def push(self):
        self.s.append(deepcopy(self.s[-1]))
        self.d.append({})

    def pop(self):
        assert len(self.s) > 1
        self.s.pop()
        self.d.pop()

    def peek(self, last=0):
        return self.d[-1-last]

def nothing(*args, **kwargs):
    pass

def text(x):#将任何type转成字符串
    if type(x) is str:
        return x
    if x is not None:
        return str(x.getText())

def flatten(l):#消除list结构
    r = []
    for i in l:
        if type(i) is list:
            r += flatten(i)
        else:
            r += [i]
    return r

def incOrInit(d:dict, key, init=0):#计数器
    if key in d:
        d[key] += 1
    else:
        d[key] = init

def listFind(f, l):#从list中查找某一value
    for i, v in enumerate(l):
        if f(v):
            return i, v
    return None

def getSymbolicNames(Lexer:type):
    intAttrs = set([a for a in dir(Lexer) if type(getattr(Lexer, a)) is int])
    ignoreAttrs = { "DEFAULT_MODE", "DEFAULT_TOKEN_CHANNEL", "HIDDEN",
            "MAX_CHAR_VALUE", "MIN_CHAR_VALUE", "MORE", "SKIP" }
    symNames = intAttrs - ignoreAttrs
    return {getattr(Lexer, a): a for a in symNames}
    
def fromListToDict(lst:list):
    dst = {}
    for (keys, value) in lst:
        for key in keys:
            dst[key] = value
    return dst

def dumpLexerTokens(lexer):
    symNames = getSymbolicNames(type(lexer))
    print(f"{'Token':<10} {'Text':<20}")
    print(f"{'-'*9:<10} {'-'*19:<20}")
    for token in lexer.getAllTokens():
        symName = symNames[token.type]
        print(f"{symName:<10} {token.text:<40}")

def prod(l):
    s = 1
    for i in l:
        s *= i
    return s

unaryOps = ['-', '!', '~']
unaryOpStrs = ['neg', 'lnot', 'not']
strOfUnaryOp = {o: s for (o, s) in zip(unaryOps, unaryOpStrs)}#将符号和IR指令对应起来

binaryOps = ['+', '-', '*', '/', '%', "==", "!=", "<", "<=", ">", ">=", "&&", "||"]
binaryOpStrs = ["add", "sub", "mul", "div", "rem", "eq", "ne", "lt", "le", "gt", "ge", "land", "lor"]
strOfBinaryOp = {o: s for (o, s) in zip(binaryOps, binaryOpStrs)}
branchOps = ["bnez", "beq", "br", "beqz"]
eqOps = ["==", "!="]
relOps = ["<", "<=", ">", ">="]
logicOps = ["&&", "||"]