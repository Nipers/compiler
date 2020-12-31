from ..utils import *
from ..generated.MiniDecafParser import MiniDecafParser
from ..generated.MiniDecafVisitor import MiniDecafVisitor

class Variable:
    _Counts = {}
    def __init__(self, name:str, offset:int, size:int=INT_BYTES):
        incOrInit(Variable._Counts, name)
        self.id = Variable._Counts[name]
        self.name = name
        self.offset = offset
        self.size = size

    def __eq__(self, another):
        return self.name == another.name and self.id == another.id\
             and self.offset == another.offset and self.size == another.size
        
    def __str__(self):
        return f"{self.name}:{self.id}"
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.name, self.id, self.offset, self.size))

class FunctionInfo:
    def __init__(self, defined=True):
        self.variables = {}
        self.positions = {}
        self.blockslots = {}
        self.defined = defined
    
    def bind(self, name, variable, position):
        self.variables[name] = variable
        self.positions[name] = position

    def __getitem__(self, name):        
        return self.variables[name]

    def __str__(self):
        return "function info"

class GlobalVarInfo:
    def __init__(self, variable:Variable, size: int, init = None):
        self.variable = variable
        self.size = size
        self.init = init

    def getInited(self):
        if self.init is not None:
            return f"initilizer = {self.init}"
        else:
            return "uninitilized"

class NameInfo:
    def __init__(self):
        self.functioninfo = {}
        self.variables = {}
        self.globalvarinfo = {}

    def __getitem__(self, ctx):
        return self.variables[ctx]

    # def addFunction(self, name, funcinfo, paraminfo):
    #     self.functioninfo[name] = funcinfo
    #     self.parameterinfo[name] = paraminfo

    def freeze(self):
        for funcNameInfo in self.functioninfo.values():
            self.variables.update(funcNameInfo.variables)



class NameManager(MiniDecafVisitor):
    def __init__(self):
        self.check = False
        self.variables = [{}]
        self.decal = [{}]
        self.n_Slots = []
        self.currentSlot = 0
        self.nameinfo = NameInfo()
        self.currentFunctionInfo = None
        self.curFuncName = None
    
    def defVar(self, ctx, num=1):
        self.currentSlot += num
        variable = self.decal[-1][text(ctx.Ident())] = self.variables[-1][text(ctx.Ident())] = Variable(text(ctx.Ident()), -INT_BYTES * self.currentSlot, INT_BYTES * num)
        position = (ctx.start.line, ctx.start.column)
        self.currentFunctionInfo.bind(ctx.Ident(), variable, position)

    def useVar(self, ctx):
        position = (ctx.start.line, ctx.start.column)
        self.currentFunctionInfo.bind(ctx.Ident(), self.variables[-1][text(ctx.Ident())], position)

    def declNElems(self, ctx:MiniDecafParser.DeclContext):
        res = prod([int(text(x)) for x in ctx.Integer()])
        if res <= 0:
            raise MiniDecafLocatedError(ctx, "array size <= 0")
        if res >= MAX_INT:
            raise MiniDecafLocatedError(ctx, "array size too large")
        return res
    
    def enterScope(self, ctx):
        self.variables.append(deepcopy(self.variables[-1]))
        self.decal.append({})
        self.n_Slots.append(self.currentSlot)
    
    def exitScope(self, ctx):
        self.currentFunctionInfo.blockslots[ctx] = self.currentSlot - self.n_Slots[-1]
        self.currentSlot = self.n_Slots[-1]
        self.variables.pop()
        self.decal.pop()
        self.n_Slots.pop()
    
    def enterAndExit(self, ctx):
        self.enterScope(ctx)
        self.visitChildren(ctx)
        self.exitScope(ctx)
        
    def visitCompound(self, ctx:MiniDecafParser.CompoundContext):
        self.enterAndExit(ctx)
    
    def visitFunc(self, ctx:MiniDecafParser.FuncContext):
        return self.visitChildren(ctx)

    def visitDecl(self, ctx:MiniDecafParser.DeclContext):
        if ctx.expr() is not None:#declare and assign
            ctx.expr().accept(self)
        name = text(ctx.Ident())
        if name in self.decal[-1]:
            raise MiniDecafLocatedError(ctx, f"redeclaretion of {name}")
        self.defVar(ctx, self.declNElems(ctx))

    
    def visitIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        ident = text(ctx.Ident())
        if ident not in self.variables[-1]:
            raise MiniDecafLocatedError(ctx, f"{ident} is not declared")
        self.useVar(ctx)

    def visitDeclForStmt(self, ctx:MiniDecafParser.DeclForStmtContext):
        self.enterAndExit(ctx)
    
    
    def visitFuncDef(self, ctx:MiniDecafParser.FuncDeclContext):
        func = text(ctx.Ident())
        if func in self.nameinfo.functioninfo and\
                self.nameinfo.functioninfo[func].defined:
            raise MiniDecafLocatedError(f"redefinition of function {func}")
        funcNameInfo = FunctionInfo(defined = True)
        self.currentFunctionInfo = self.nameinfo.functioninfo[func] = funcNameInfo
        self.enterScope(ctx.compound())
        ctx.paramList().accept(self)
        # skip the enter/exitScope of the block because we've already done it.
        self.visitChildren(ctx.compound())
        self.exitScope(ctx.compound())
        self.currentFunctionInfo = None
    
    def visitFuncDecl(self, ctx:MiniDecafParser.FuncDefContext):
        func = text(ctx.Ident())
        if func in self.nameinfo.globalvarinfo:
            raise MiniDecafLocatedError(ctx, f"global variable {func} redeclared as function")
        funcNameInfo = FunctionInfo(defined=False)
        if func not in self.nameinfo.functioninfo:
            self.nameinfo.functioninfo[func] = funcNameInfo

    def visitParamList(self, ctx:MiniDecafParser.ParamListContext):
        self.visitChildren(ctx)
        def f(decl):
            return self.variables[-1][text(decl.Ident())]
        return list(map(f, ctx.decl()))

    def globalInitializer(self, ctx:MiniDecafParser.ExprContext):
        if ctx is None:
            return None
        return safeEval(text(ctx))
        
    def visitGlobal(self, ctx:MiniDecafParser.GlobalContext):
        ctx = ctx.decl()
        inital = self.globalInitializer(ctx.expr())
        name = text(ctx.Ident())
        if name in self.nameinfo.functioninfo:
            raise MiniDecafLocatedError(ctx, f"function {name} redeclared as global variable")
        variable = Variable(name, None, INT_BYTES * self.declNElems(ctx))
        globalInfo = GlobalVarInfo(variable, INT_BYTES * self.declNElems(ctx), inital)
        if name in self.decal[-1]:
            oldGlobalInfo = self.nameinfo.globalvarinfo[name]
            if oldGlobalInfo.init is not None and globalInfo.init is not None:
                raise MiniDecafLocatedError(ctx, f"redefinition of global variable {name}")
            if globalInfo.init is not None:
                self.nameinfo.globalvarinfo[oldVar].init = inital
        else:
            self.decal[-1][name] = self.variables[-1][name] = variable
            self.nameinfo.globalvarinfo[name] = globalInfo
        
    def visitProg(self, ctx:MiniDecafParser.ProgContext):
        self.visitChildren(ctx)
        self.nameinfo.freeze()