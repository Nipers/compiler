# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniDecafParser import MiniDecafParser
else:
    from MiniDecafParser import MiniDecafParser

# This class defines a complete listener for a parse tree produced by MiniDecafParser.
class MiniDecafListener(ParseTreeListener):

    # Enter a parse tree produced by MiniDecafParser#prog.
    def enterProg(self, ctx:MiniDecafParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#prog.
    def exitProg(self, ctx:MiniDecafParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#func.
    def enterFunc(self, ctx:MiniDecafParser.FuncContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#func.
    def exitFunc(self, ctx:MiniDecafParser.FuncContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#global.
    def enterGlobal(self, ctx:MiniDecafParser.GlobalContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#global.
    def exitGlobal(self, ctx:MiniDecafParser.GlobalContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#funcDef.
    def enterFuncDef(self, ctx:MiniDecafParser.FuncDefContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#funcDef.
    def exitFuncDef(self, ctx:MiniDecafParser.FuncDefContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#funcDecl.
    def enterFuncDecl(self, ctx:MiniDecafParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#funcDecl.
    def exitFuncDecl(self, ctx:MiniDecafParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#pointer.
    def enterPointer(self, ctx:MiniDecafParser.PointerContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#pointer.
    def exitPointer(self, ctx:MiniDecafParser.PointerContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#intType.
    def enterIntType(self, ctx:MiniDecafParser.IntTypeContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#intType.
    def exitIntType(self, ctx:MiniDecafParser.IntTypeContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#paramList.
    def enterParamList(self, ctx:MiniDecafParser.ParamListContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#paramList.
    def exitParamList(self, ctx:MiniDecafParser.ParamListContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#blockitem.
    def enterBlockitem(self, ctx:MiniDecafParser.BlockitemContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#blockitem.
    def exitBlockitem(self, ctx:MiniDecafParser.BlockitemContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#compound.
    def enterCompound(self, ctx:MiniDecafParser.CompoundContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#compound.
    def exitCompound(self, ctx:MiniDecafParser.CompoundContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#retStmt.
    def enterRetStmt(self, ctx:MiniDecafParser.RetStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#retStmt.
    def exitRetStmt(self, ctx:MiniDecafParser.RetStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#exprStmt.
    def enterExprStmt(self, ctx:MiniDecafParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#exprStmt.
    def exitExprStmt(self, ctx:MiniDecafParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#voidStmt.
    def enterVoidStmt(self, ctx:MiniDecafParser.VoidStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#voidStmt.
    def exitVoidStmt(self, ctx:MiniDecafParser.VoidStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#ifStmt.
    def enterIfStmt(self, ctx:MiniDecafParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#ifStmt.
    def exitIfStmt(self, ctx:MiniDecafParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cpdStmt.
    def enterCpdStmt(self, ctx:MiniDecafParser.CpdStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cpdStmt.
    def exitCpdStmt(self, ctx:MiniDecafParser.CpdStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#declForStmt.
    def enterDeclForStmt(self, ctx:MiniDecafParser.DeclForStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#declForStmt.
    def exitDeclForStmt(self, ctx:MiniDecafParser.DeclForStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#forStmt.
    def enterForStmt(self, ctx:MiniDecafParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#forStmt.
    def exitForStmt(self, ctx:MiniDecafParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#whileStmt.
    def enterWhileStmt(self, ctx:MiniDecafParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#whileStmt.
    def exitWhileStmt(self, ctx:MiniDecafParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#doWhileStmt.
    def enterDoWhileStmt(self, ctx:MiniDecafParser.DoWhileStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#doWhileStmt.
    def exitDoWhileStmt(self, ctx:MiniDecafParser.DoWhileStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#breakStmt.
    def enterBreakStmt(self, ctx:MiniDecafParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#breakStmt.
    def exitBreakStmt(self, ctx:MiniDecafParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#continueStmt.
    def enterContinueStmt(self, ctx:MiniDecafParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#continueStmt.
    def exitContinueStmt(self, ctx:MiniDecafParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#decl.
    def enterDecl(self, ctx:MiniDecafParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#decl.
    def exitDecl(self, ctx:MiniDecafParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#expr.
    def enterExpr(self, ctx:MiniDecafParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#expr.
    def exitExpr(self, ctx:MiniDecafParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tAsgn.
    def enterTAsgn(self, ctx:MiniDecafParser.TAsgnContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tAsgn.
    def exitTAsgn(self, ctx:MiniDecafParser.TAsgnContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cAsgn.
    def enterCAsgn(self, ctx:MiniDecafParser.CAsgnContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cAsgn.
    def exitCAsgn(self, ctx:MiniDecafParser.CAsgnContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tCond.
    def enterTCond(self, ctx:MiniDecafParser.TCondContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tCond.
    def exitTCond(self, ctx:MiniDecafParser.TCondContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cCond.
    def enterCCond(self, ctx:MiniDecafParser.CCondContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cCond.
    def exitCCond(self, ctx:MiniDecafParser.CCondContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cLor.
    def enterCLor(self, ctx:MiniDecafParser.CLorContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cLor.
    def exitCLor(self, ctx:MiniDecafParser.CLorContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tLor.
    def enterTLor(self, ctx:MiniDecafParser.TLorContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tLor.
    def exitTLor(self, ctx:MiniDecafParser.TLorContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cLand.
    def enterCLand(self, ctx:MiniDecafParser.CLandContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cLand.
    def exitCLand(self, ctx:MiniDecafParser.CLandContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tland.
    def enterTland(self, ctx:MiniDecafParser.TlandContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tland.
    def exitTland(self, ctx:MiniDecafParser.TlandContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tEq.
    def enterTEq(self, ctx:MiniDecafParser.TEqContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tEq.
    def exitTEq(self, ctx:MiniDecafParser.TEqContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cEq.
    def enterCEq(self, ctx:MiniDecafParser.CEqContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cEq.
    def exitCEq(self, ctx:MiniDecafParser.CEqContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#eqOp.
    def enterEqOp(self, ctx:MiniDecafParser.EqOpContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#eqOp.
    def exitEqOp(self, ctx:MiniDecafParser.EqOpContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tRel.
    def enterTRel(self, ctx:MiniDecafParser.TRelContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tRel.
    def exitTRel(self, ctx:MiniDecafParser.TRelContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cRel.
    def enterCRel(self, ctx:MiniDecafParser.CRelContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cRel.
    def exitCRel(self, ctx:MiniDecafParser.CRelContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#relOp.
    def enterRelOp(self, ctx:MiniDecafParser.RelOpContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#relOp.
    def exitRelOp(self, ctx:MiniDecafParser.RelOpContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cAdd.
    def enterCAdd(self, ctx:MiniDecafParser.CAddContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cAdd.
    def exitCAdd(self, ctx:MiniDecafParser.CAddContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tAdd.
    def enterTAdd(self, ctx:MiniDecafParser.TAddContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tAdd.
    def exitTAdd(self, ctx:MiniDecafParser.TAddContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#addOp.
    def enterAddOp(self, ctx:MiniDecafParser.AddOpContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#addOp.
    def exitAddOp(self, ctx:MiniDecafParser.AddOpContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tMul.
    def enterTMul(self, ctx:MiniDecafParser.TMulContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tMul.
    def exitTMul(self, ctx:MiniDecafParser.TMulContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cMul.
    def enterCMul(self, ctx:MiniDecafParser.CMulContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cMul.
    def exitCMul(self, ctx:MiniDecafParser.CMulContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cCast.
    def enterCCast(self, ctx:MiniDecafParser.CCastContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cCast.
    def exitCCast(self, ctx:MiniDecafParser.CCastContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tCast.
    def enterTCast(self, ctx:MiniDecafParser.TCastContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tCast.
    def exitTCast(self, ctx:MiniDecafParser.TCastContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#mulOp.
    def enterMulOp(self, ctx:MiniDecafParser.MulOpContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#mulOp.
    def exitMulOp(self, ctx:MiniDecafParser.MulOpContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tUnary.
    def enterTUnary(self, ctx:MiniDecafParser.TUnaryContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tUnary.
    def exitTUnary(self, ctx:MiniDecafParser.TUnaryContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#cUnary.
    def enterCUnary(self, ctx:MiniDecafParser.CUnaryContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#cUnary.
    def exitCUnary(self, ctx:MiniDecafParser.CUnaryContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#array.
    def enterArray(self, ctx:MiniDecafParser.ArrayContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#array.
    def exitArray(self, ctx:MiniDecafParser.ArrayContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#funcCall.
    def enterFuncCall(self, ctx:MiniDecafParser.FuncCallContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#funcCall.
    def exitFuncCall(self, ctx:MiniDecafParser.FuncCallContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#tPostfix.
    def enterTPostfix(self, ctx:MiniDecafParser.TPostfixContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#tPostfix.
    def exitTPostfix(self, ctx:MiniDecafParser.TPostfixContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#argList.
    def enterArgList(self, ctx:MiniDecafParser.ArgListContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#argList.
    def exitArgList(self, ctx:MiniDecafParser.ArgListContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#imme.
    def enterImme(self, ctx:MiniDecafParser.ImmeContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#imme.
    def exitImme(self, ctx:MiniDecafParser.ImmeContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#identifer.
    def enterIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#identifer.
    def exitIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#expression.
    def enterExpression(self, ctx:MiniDecafParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#expression.
    def exitExpression(self, ctx:MiniDecafParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#unaryOp.
    def enterUnaryOp(self, ctx:MiniDecafParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#unaryOp.
    def exitUnaryOp(self, ctx:MiniDecafParser.UnaryOpContext):
        pass



del MiniDecafParser