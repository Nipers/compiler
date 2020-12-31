from ..generated.MiniDecafParser import MiniDecafParser
from ..generated.MiniDecafVisitor import MiniDecafVisitor
from .instructor import *
from ..utils import *
from .NameManager import NameInfo, Variable
from .TypeChecker import *

class LabelManager:#用于管理标签
    def __init__(self):
        self.labels = {}
        self.entry = []
        self.exit = []
    
    def newLabel(self, scope = "_L"):
        if scope not in self.labels.keys():
            self.labels[scope] = 1
        else:
            self.labels[scope] += 1
        return f"{scope}_{self.labels[scope]}"
    
    def enterLoop(self, entryLabel, exitLabel):
        self.entry.append(entryLabel)
        self.exit.append(exitLabel)
    
    def exitLoop(self):
        self.exit.pop()
        self.entry.pop()
    
    def breakLabel(self):
        if len(self.exit) < 1:
            raise MiniDecafLocatedError("This Break is not in a loop")
        return self.exit[-1]

    def continueLabel(self):
        if len(self.exit) < 1:
            raise MiniDecafLocatedError("This Continue is not in a loop")
        return self.entry[-1]


class StackIRGen(MiniDecafVisitor):
    def __init__(self, emitter, nameInfo:NameInfo, typeInfo:TypeInfo):
        self.emitter = emitter
        self.labelmanager = LabelManager()
        self.nameInfo = nameInfo
        self.typeInfo = typeInfo
        self.curFuncInfo = None

    def getVar(self, name):
        return self.nameInfo[name]

    def emitVar(self, var:Variable):
        if var.offset is None:
            self.emitter([GlobalSymbol(var.name)])
        else:
            self.emitter([FrameSlot(var.offset)])
    

    def visitRetStmt(self, ctx:MiniDecafParser.RetStmtContext):
        self.emitter([Comment("Ret")])
        self.visitChildren(ctx)
        self.emitter([Ret()])

    def visitExprStmt(self, ctx:MiniDecafParser.ExprStmtContext):
        self.emitter([Comment("Expr")])
        self.visitChildren(ctx)
        self.emitter([Pop()])

    def visitIfStmt(self, ctx:MiniDecafParser.IfStmtContext):
        self.emitter([Comment("If")])
        ctx.expr().accept(self)
        Exit = self.labelmanager.newLabel("if_exit")
        Else = self.labelmanager.newLabel("if_else")
        if ctx.els is not None:
            self.emitter([Branch("beqz", Else)])
            ctx.then.accept(self)
            self.emitter([Branch("br", Exit)])
            self.emitter([Label(Else)]);
            ctx.els.accept(self)
            self.emitter([Label(Exit)])
        else:
            self.emitter([Branch("beqz", Exit)])
            ctx.then.accept(self)
            self.emitter([Label(Exit)])

    def visitCompound(self, ctx:MiniDecafParser.CompoundContext):
        self.emitter([Comment("Enter Compound")])
        self.visitChildren(ctx)
        self.emitter([Pop()] * self.nameInfo.functioninfo[self.curFuncInfo].blockslots[ctx])
        self.emitter([Comment("Exit Compound")])

    def loop(self, name, init, cond, post, body):
        entryLabel = self.labelmanager.newLabel(f"{name}_Entry")
        if post is not None:
            continueLabel = self.labelmanager.newLabel(f"{name}_Continue")
        else:
            continueLabel = entryLabel
        exitLabel = self.labelmanager.newLabel(f"{name}_Exit")
        self.labelmanager.enterLoop(continueLabel, exitLabel)
        if init is not None:
            init.accept(self)
            if isinstance(init, MiniDecafParser.ExprContext):
                self.emitter([Pop()])
        self.emitter([Label(entryLabel)])
        if cond is not None:
            cond.accept(self)
        else:
            self.emitter([Const(1)])#永真
        self.emitter([Branch("beqz", exitLabel)])
        body.accept(self)
        if post is not None:
            self.emitter([Label(continueLabel)])
            post.accept(self)
            if isinstance(post, MiniDecafParser.ExprContext):
                self.emitter([Pop()])
        self.emitter([Branch("br", entryLabel)])
        self.emitter([Label(exitLabel)])
        self.labelmanager.exitLoop()

    def visitDeclForStmt(self, ctx:MiniDecafParser.DeclForStmtContext):
        self.loop("for", ctx.init, ctx.ctrl, ctx.post, ctx.stmt())
        self.emitter([Pop()] * self.nameInfo.functioninfo[self.curFuncInfo].blockslots[ctx])

    def visitForStmt(self, ctx:MiniDecafParser.ForStmtContext):
        self.loop("for", ctx.init, ctx.ctrl, ctx.post, ctx.stmt())

    def visitWhileStmt(self, ctx:MiniDecafParser.WhileStmtContext):
        self.loop("while", None, ctx.expr(), None, ctx.stmt())

    def visitDoWhileStmt(self, ctx:MiniDecafParser.DoWhileStmtContext):
        self.loop("dowhile", ctx.stmt(), ctx.expr(), None, ctx.stmt())
    
    def visitBreakStmt(self, ctx:MiniDecafParser.BreakStmtContext):
        self.emitter([Branch("br", self.labelmanager.breakLabel())])
    
    def visitContinueStmt(self, ctx:MiniDecafParser.ContinueStmtContext):
        self.emitter([Branch("br", self.labelmanager.continueLabel())])
    
    def visitImme(self, ctx:MiniDecafParser.ImmeContext):
        self.emitter([Const(int(text(ctx.Integer())))])
    
    def visitCUnary(self, ctx:MiniDecafParser.CUnaryContext):
        op = text(ctx.unaryOp())
        if op == '&':
            self.emitLoc(ctx.cast())
        elif op == '*':
            self.visitChildren(ctx)
            self.emitter([Load()])
        else:
            self.visitChildren(ctx)
            self.emitter([Unary(op)])
    
    def visitCAdd(self, ctx:MiniDecafParser.CAddContext):
        op = text(ctx.addOp())
        lhs = ctx.add()
        rhs = ctx.mul()
        #依据lhs和rhs的类型将运算分为四种，分别处理
        if isinstance(self.typeInfo[lhs], Pointer):
            size = self.typeInfo[lhs].size()
            lhs.accept(self)
            rhs.accept(self)
            if isinstance(self.typeInfo[rhs], Pointer):
                self.emitter([Binary(op)])
                self.emitter([Const(size), Binary('/')])
            else:
                self.emitter([Const(size), Binary('*')])
                self.emitter([Binary(op)])
        else:
            size = self.typeInfo[rhs].size()
            if isinstance(self.typeInfo[rhs], Pointer):
                lhs.accept(self)
                self.emitter([Const(size), Binary('*')])
                rhs.accept(self)
                self.emitter([Binary(op)])
            else:
                self.visitChildren(ctx)
                self.emitter([Binary(op)])


    def visitCMul(self, ctx:MiniDecafParser.CMulContext):
        self.visitChildren(ctx)
        self.emitter([Binary(text(ctx.mulOp()))])
    
    def visitCRel(self, ctx:MiniDecafParser.CRelContext):
        self.visitChildren(ctx)
        self.emitter([Binary(text(ctx.relOp()))])
    
    def visitCEq(self, ctx:MiniDecafParser.CEqContext):
        self.visitChildren(ctx)
        self.emitter([Binary(text(ctx.eqOp()))])
    
    #将And和Lor改写为短路代码
    def visitCLand(self, ctx:MiniDecafParser.CLandContext):
        falseLabel = self.labelmanager.newLabel("land_false")
        exitLabel = self.labelmanager.newLabel("land_exit")
        ctx.land().accept(self)
        self.emitter([Branch("beqz", falseLabel)])
        ctx.eq().accept(self)
        self.emitter([Branch("beqz", falseLabel), Const(1), Branch("br", exitLabel),
            Label(falseLabel), Const(0), Label(exitLabel)])

    def visitCLor(self, ctx:MiniDecafParser.CLorContext):
        truelabel = self.labelmanager.newLabel("lor_true")
        exitlabel = self.labelmanager.newLabel("lor_exit")
        ctx.lor().accept(self)
        self.emitter([Branch("bnez", truelabel)])
        ctx.land().accept(self)
        self.emitter([Branch("bnez", truelabel), Const(0), Branch("br", exitlabel),
            Label(truelabel), Const(1), Label(exitlabel)])

    
    def visitDecl(self, ctx:MiniDecafParser.DeclContext):
        variable = self.getVar(ctx.Ident())#变量名
        if ctx.expr() is not None:#命名的同时有没有赋值
            ctx.expr().accept(self)#计算赋给变量的值
        else:
            self.emitter([Const(0)] * (variable.size//INT_BYTES))#默认值为0
        self.emitter([Comment(f"[ir-offset]: {variable} -> {variable.offset}")])

    def visitGlobal(self, ctx:MiniDecafParser.GlobalContext):
        pass

    def visitIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        variable = self.getVar(ctx.Ident())
        self.emitVar(variable)
        if not isinstance(self.typeInfo[ctx], Array):
            self.emitter([Load()])

    def emitLoc(self, value:MiniDecafParser.ExprContext):
        loc = self.typeInfo.lvalueLoc(value)
        for locStep in loc:
            if isinstance(locStep, IRInstr):
                self.emitter([locStep])
            else:
                locStep.accept(self)
    
    def visitCAsgn(self, ctx:MiniDecafParser.CAsgnContext):
        ctx.asgn().accept(self)
        self.emitLoc(ctx.unary())
        self.emitter([Store()])
    
    def visitCCond(self, ctx:MiniDecafParser.CCondContext):#利用了短路的方法
        ctx.lor().accept(self)
        exitLabel = self.labelmanager.newLabel("Cond_end")
        elseLabel = self.labelmanager.newLabel("Cond_else")
        self.emitter([Branch("beqz", elseLabel)])
        ctx.expr().accept(self)
        self.emitter([Branch("br", exitLabel), Label(elseLabel)])
        ctx.cond().accept(self)
        self.emitter([Label(exitLabel)])

    def visitFuncDef(self, ctx:MiniDecafParser.FuncDefContext):
        funcName = text(ctx.Ident())
        nParams = len(self.typeInfo.funcs[funcName].paramTp)
        self.curFuncInfo = funcName
        self.emitter.enterFunction(funcName, nParams)
        ctx.compound().accept(self)
        self.emitter.exitFunction()
        self.curFuncInfo = None

    def visitFuncDecl(self, ctx:MiniDecafParser.FuncDeclContext):
        pass
    
    def visitFuncCall(self, ctx:MiniDecafParser.FuncCallContext):
        arguments = ctx.argList().expr()
        lens = len(arguments)
        for argument in reversed(arguments):
            argument.accept(self)
        funcName = text(ctx.Ident())
        self.emitter([FuncCall(funcName)])

    def visitArray(self, ctx:MiniDecafParser.ArrayContext):
        fixupMult = self.typeInfo[ctx.postfix()].base.size()
        ctx.postfix().accept(self)
        ctx.expr().accept(self)
        self.emitter([Const(fixupMult), Binary('*'), Binary('+')])
        if not isinstance(self.typeInfo[ctx], Array):
            self.emitter([Load()])
        

    def visitProg(self, ctx:MiniDecafParser.ProgContext):
        for globalInfo in self.nameInfo.globalvarinfo.values():
            self.emitter.emitGlobal(globalInfo)
        self.visitChildren(ctx)