from .instructor import IRInstr, Comment, Label
from .NameManager import GlobalVarInfo, NameManager
from .TypeChecker import TypeChecker
from .irgen import StackIRGen
class IRFunc:
    def __init__(self, name:str, paramNum:int, instrs:[IRInstr]):
        self.name = name
        self.paramNum = paramNum
        self.instrs = instrs

    def __str__(self):
        def convert(instr):
            if type(instr) is Comment:
                return f"\t\t\t\t{instr}"
            if type(instr) is Label:
                return f"{instr}"
            return f"\t{instr}"
        body = "\n".join(map(convert, self.instrs))
        return f"{self.name}({self.paramNum}):\n{body}"


class IRGlobal:
    def __init__(self, sym:str, size:int, init = None, align = 8):
        self.sym = sym
        self.size = size
        self.init = init
        self.align = align
    
    def initStr(self):
        if self.init is None:
            return "uninitilized"
        else:
            return f"initilizer = {self.init}"

def transfer(globalInfo:GlobalVarInfo):
    assert globalInfo.variable.offset is None
    return IRGlobal(globalInfo.variable.name, globalInfo.size, globalInfo.init)



class IRProg:
    def __init__(self, funcs:[IRFunc], globs:[IRGlobal]):
        self.funcs = funcs
        self.globs = globs

    def __str__(self):
        globs = "\n".join(map(str, self.globs))
        funcs = "\n\n".join(map(str, self.funcs))
        return "========Globs:\n" + globs + "\n\n========Funcs:\n" + funcs

class IREmitter:
    def __init__(self):
        self.functions = []
        self.globals = []
        self.curFuncName = None
        self.curParamNum = None
        self.curInstrs = []
    
    def emit(self, irs:[IRInstr]):
        self.curInstrs += irs

    def enterFunction(self, funcName:str, paramNum:int):
        self.curFuncName = funcName
        self.curParamNum = paramNum
        self.curInstrs = []

    def exitFunction(self):
        self.functions.append(IRFunc(self.curFuncName, self.curParamNum, self.curInstrs))

    def getIR(self):#
        return IRProg(self.functions, self.globals)

    def emitGlobal(self, globalInfo:GlobalVarInfo):
        self.globals += [transfer(globalInfo)]

    def __call__(self, irs:[IRInstr]):
        self.emit(irs)


def GenerateName(tree):
    nameManager = NameManager()
    nameManager.visit(tree)
    return nameManager.nameInfo


def typeCheck(tree, nameInfo):
    typeCheckr = TypeChecker(nameInfo)
    typeCheckr.visit(tree)
    return typeCheckr.typeInfo


def irGen(tree, nameInfo, typeInfo):
    irEmitter = IREmitter()
    StackIRGen(irEmitter, nameInfo, typeInfo).visit(tree)
    return irEmitter.getIR()