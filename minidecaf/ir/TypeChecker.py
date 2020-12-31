from ..utils import *
from ..generated.MiniDecafParser import MiniDecafParser
from ..generated.MiniDecafVisitor import MiniDecafVisitor
from ..ir.instructor import *
from .NameManager import *
from .Types import *

class TypeInfo:
    def __init__(self):
        self.locs = {}
        self.funcs = {}
        self.types = {}
    
    def lvalueLoc(self, ctx):
        return self.locs[ctx]
    
    def setlvalueLoc(self, ctx, loc:list):
        self.locs[ctx] = loc
    
    def __str__(self):
        result = "lvalue analysis result: (location of expressiong at lhs == rhs:\n\t"
        def p(ctx):
            return f"{ctx.start.line}, {ctx.start.column} ~ {ctx.stop.line}, {ctx.stop.column}"
        def g(locStep):
            if isinstance(locStep, IRInstr):
                return f"{locStep}"
            return f"[{p(locStep)}]"
        def func(cl):
            ctx, loc = cl
            ctxStr = f"{p(ctx)}"
            locStr = " :: ".join(map(g, loc))
            return f"{ctxStr:>32} : {locStr}"
        result += "\n\t".join(map(func, self.locs.items()))
        result += "\n\n TypeInfo for funcs:\n\t"
        def fun(nf):
            name, funcInfo = nf
            return f"{name:>32} : ({funcInfo.paramTp})"
        result += "\n\t".join(map(fun, self.funcs.items()))
        return result
        
    def __getitem__(self, ctx):
        return self.types[ctx]

class FuncTypeInfo:
    def __init__(self, retTp:Type, paramTp:list):
        self.retTp = retTp
        self.paramTp = paramTp
    
    def compare(self, value):
        return self.retTp == value.retTp and self.paramTp == value.paramTp
    
    def call(self):
        @TypeRule
        def callRule(ctx, argTp:list):
            if self.paramTp == argTp:
                return self.retTp
            return "Wrong arguments"
        return callRule
    
def SaveType(func):
    def save(self, ctx):
        tp = func(self, ctx)
        self.typeInfo.types[ctx] = tp
        return tp
    return save

class TypeChecker(MiniDecafVisitor):
    def __init__(self, nameinfo: NameInfo):
        self.varType = {}
        self.nameInfo = nameinfo
        self.curFunc = None
        self.typeInfo = TypeInfo()
        self.locator = Locator(self.nameInfo, self.typeInfo)

    def visitChildren(self, node):
        self.typeInfo.types[node] = MiniDecafVisitor.visitChildren(self, node)
        return self.typeInfo.types[node]

    def getVar(self, name):
        return self.nameInfo[name]

    def declType(self, ctx:MiniDecafParser.DeclContext):
        base = ctx.tp().accept(self)
        dims = [int(text(i)) for i in reversed(ctx.Integer())]
        if len(dims) == 0:
            return base
        return make(base, dims)

    def funcTypeInfo(self, ctx):
        retTp = ctx.tp().accept(self)
        paramTp = self.paramTp(ctx.paramList())
        return FuncTypeInfo(retTp, paramTp)

    def argTp(self, ctx:MiniDecafParser.ArgListContext):
        return list(map(lambda i: i.accept(self), ctx.expr()))

    def visitPointer(self, ctx:MiniDecafParser.PointerContext):
        return Pointer(ctx.tp().accept(self))

    def visitIntType(self, ctx:MiniDecafParser.IntTypeContext):
        return Int()
    
    def locate(self, ctx):
        location = self.locator.locate(self.curFunc, ctx)
        if location is None:
            raise MiniDecafLocatedError(ctx, "lvalue expected")
        self.typeInfo.setlvalueLoc(ctx, location)

    def checkUnary(self, ctx, op:str, tp:Type):
        rule = fromListToDict([
            (unaryOps, intUnaRule),
            (['&'],    addrofRule),
            (['*'],    derefRule),
        ])[op]
        return rule(ctx, tp)
    
    def checkBinary(self, ctx, op:str, lhs:Type, rhs:Type):
        rule = fromListToDict([
            (['*', '/', '%'] + logicOps, intBinRule),
            (eqOps,                      eqRule),
            (relOps,                     relRule),
            (['='],                      asgnRule),
            (['+'],                      tryAll('+', intBinRule, pointerCalRule)),
            (['-'],                      tryAll('-', intBinRule, pointerCalRule, pointerDiffRule)),
        ])[op]
        return rule(ctx, lhs, rhs)

    @SaveType
    def visitCCast(self, ctx:MiniDecafParser.CCastContext):
        ctx.cast().accept(self)
        return ctx.tp().accept(self)

    @SaveType
    def visitCUnary(self, ctx:MiniDecafParser.CUnaryContext):
        result = self.checkUnary(ctx.unaryOp(), text(ctx.unaryOp()), ctx.cast().accept(self))
        if text(ctx.unaryOp()) == '&':
            self.locate(ctx.cast())
        return result

    @SaveType
    def visitExpression(self, ctx:MiniDecafParser.ExpressionContext):
        return ctx.expr().accept(self)

    @SaveType
    def visitCAdd(self, ctx:MiniDecafParser.CAddContext):
        return self.checkBinary(ctx.addOp(), text(ctx.addOp()),
            ctx.add().accept(self), ctx.mul().accept(self))

    @SaveType
    def visitCMul(self, ctx:MiniDecafParser.CMulContext):
        return self.checkBinary(ctx.mulOp(), text(ctx.mulOp()),
            ctx.mul().accept(self), ctx.cast().accept(self))

    @SaveType
    def visitCRel(self, ctx:MiniDecafParser.CRelContext):
        return self.checkBinary(ctx.relOp(), text(ctx.relOp()),
            ctx.rel().accept(self), ctx.add().accept(self))

    @SaveType
    def visitCEq(self, ctx:MiniDecafParser.CEqContext):
        return self.checkBinary(ctx.eqOp(), text(ctx.eqOp()),
            ctx.eq().accept(self), ctx.rel().accept(self))

    @SaveType
    def visitCLand(self, ctx:MiniDecafParser.CLandContext):
        return self.checkBinary(ctx, '&&',
            ctx.land().accept(self), ctx.eq().accept(self))

    @SaveType
    def visitCLor(self, ctx:MiniDecafParser.CLorContext):
        return self.checkBinary(ctx, '||',
            ctx.lor().accept(self), ctx.land().accept(self))

    @SaveType
    def visitCCond(self, ctx:MiniDecafParser.CCondContext):
        return condRule(ctx, ctx.lor().accept(self),
            ctx.expr().accept(self), ctx.cond().accept(self))

    @SaveType
    def visitCAsgn(self, ctx:MiniDecafParser.CAsgnContext):
        res = self.checkBinary(ctx.Equal(), text(ctx.Equal()),
            ctx.unary().accept(self), ctx.asgn().accept(self))
        self.locate(ctx.unary())
        return res

    @SaveType
    def visitFuncCall(self, ctx:MiniDecafParser.FuncCallContext):
        argTp = self.argTp(ctx.argList())
        funcName = text(ctx.Ident())
        rule = self.typeInfo.funcs[funcName].call()
        return rule(ctx, argTp)

    @SaveType
    def visitArray(self, ctx:MiniDecafParser.ArrayContext):
        return arrayRule(ctx, ctx.postfix().accept(self), ctx.expr().accept(self))

    @SaveType
    def visitImme(self, ctx:MiniDecafParser.ImmeContext):
        from ast import literal_eval
        if literal_eval(text(ctx)) == 0:
            return Zero()
        return Int()

    @SaveType
    def visitIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        return self.varType[self.getVar(ctx.Ident())]

    def visitDecl(self, ctx:MiniDecafParser.DeclContext):
        tp = self.declType(ctx)
        self.varType[self.getVar(ctx.Ident())] = tp
        if ctx.expr() is not None:
            initType = ctx.expr().accept(self)
            asgnRule(ctx, tp, initType)
    
    def checkFunc(self, ctx):
        funcTypeInfo = self.funcTypeInfo(ctx)
        funcName = text(ctx.Ident())
        if funcName in self.typeInfo.funcs:
            preFuncTypeInfo = self.typeInfo.funcs[funcName]
            if not funcTypeInfo.compare(preFuncTypeInfo):
                raise MiniDecafLocatedError(ctx, f"confliced types for {funcName}")
        self.typeInfo.funcs[funcName] = funcTypeInfo

    def visitFuncDef(self, ctx:MiniDecafParser.FuncDefContext):
        self.curFunc = text(ctx.Ident())
        self.checkFunc(ctx)
        self.visitChildren(ctx)
        self.curFunc = None

    def visitFuncDecl(self, ctx:MiniDecafParser.FuncDeclContext):
        self.curFunc = funcName = text(ctx.Ident())
        self.checkFunc(ctx)
        self.curFunc = None

    def paramTp(self, ctx:MiniDecafParser.ParamListContext):
        result = []
        for decl in ctx.decl():
            if decl.expr() is not None:
                raise MiniDecafLocatedError(decl, "parameter can't have initializers")
            paramTp = self.declType(decl)
            if isinstance(paramTp, Array):
                raise MiniDecafLocatedError(decl, "array can't be parameter")
            result.append(paramTp)
        return result
    
    def visitGlobal(self, ctx:MiniDecafParser.GlobalContext):
        ctx = ctx.decl()
        var = self.nameInfo.globalvarinfo[text(ctx.Ident())].variable
        tp = self.declType(ctx)
        if var in self.varType:
            if tp != self.varType[var]:
                raise MiniDecafLocatedError(ctx, f"conflicting type for {var.name}")
        else:
            self.varType[var] = tp
        if ctx.expr() is not None:
            asgnRule(ctx, tp, ctx.expr().accept(self))

    def visitRetStmt(self, ctx:MiniDecafParser.RetStmtContext):
        retRule(ctx, self.typeInfo.funcs[self.curFunc].retTp
            ,ctx.expr().accept(self))
    
    def visitIfStmt(self, ctx:MiniDecafParser.IfStmtContext):
        self.visitChildren(ctx)
        stmtCondRule(ctx, ctx.expr().accept(self))
    
    def visitForStmt(self, ctx:MiniDecafParser.ForStmtContext):
        self.visitChildren(ctx)
        if ctx.ctrl is not None:
            stmtCondRule(ctx, ctx.ctrl.accept(self))
        
    def visitWhileStmt(self, ctx:MiniDecafParser.WhileStmtContext):
        self.visitChildren(ctx)
        stmtCondRule(ctx, ctx.expr().accept(self))

    def visitDoWhileStmt(self, ctx:MiniDecafParser.DoWhileStmtContext):
        self.visitChildren(ctx)
        stmtCondRule(ctx, ctx.expr().accept(self))

    def visitDeclForStmt(self, ctx:MiniDecafParser.DeclForStmtContext):
        self.visitChildren(ctx)
        if ctx.ctrl is not None:
            stmtCondRule(ctx, ctx.ctrl.accept(self))

class Locator(MiniDecafVisitor):
    def __init__(self, nameInfo:NameInfo, typeInfo: TypeInfo):
        self.nameInfo = nameInfo
        self.typeInfo = typeInfo

    def locate(self, funcName:str, ctx):
        self.func = funcName
        result = ctx.accept(self)
        self.func = None
        return result

    def visitIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        var = self.nameInfo[ctx.Ident()]
        if var.offset is None:
            return [GlobalSymbol(var.name)]
        return [FrameSlot(var.offset)]

    def visitCUnary(self, ctx:MiniDecafParser.CUnaryContext):
        op = text(ctx.unaryOp())
        if op == '*':
            return [ctx.cast()]

    def visitArray(self, ctx:MiniDecafParser.ArrayContext):
        fixupMult = self.typeInfo[ctx.postfix()].base.size()
        return [ctx.postfix(), ctx.expr(), Const(fixupMult), Binary('*'), Binary('+')]

    def visitExpression(self, ctx:MiniDecafParser.ExpressionContext):
        return ctx.expr().accept(self)
