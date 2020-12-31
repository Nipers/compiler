# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniDecafParser import MiniDecafParser
else:
    from MiniDecafParser import MiniDecafParser

# This class defines a complete generic visitor for a parse tree produced by MiniDecafParser.

class MiniDecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniDecafParser#prog.
    def visitProg(self, ctx:MiniDecafParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#func.
    def visitFunc(self, ctx:MiniDecafParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#global.
    def visitGlobal(self, ctx:MiniDecafParser.GlobalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#funcDef.
    def visitFuncDef(self, ctx:MiniDecafParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniDecafParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#pointer.
    def visitPointer(self, ctx:MiniDecafParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#intType.
    def visitIntType(self, ctx:MiniDecafParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#paramList.
    def visitParamList(self, ctx:MiniDecafParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#blockitem.
    def visitBlockitem(self, ctx:MiniDecafParser.BlockitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#compound.
    def visitCompound(self, ctx:MiniDecafParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#retStmt.
    def visitRetStmt(self, ctx:MiniDecafParser.RetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#exprStmt.
    def visitExprStmt(self, ctx:MiniDecafParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#voidStmt.
    def visitVoidStmt(self, ctx:MiniDecafParser.VoidStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#ifStmt.
    def visitIfStmt(self, ctx:MiniDecafParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cpdStmt.
    def visitCpdStmt(self, ctx:MiniDecafParser.CpdStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#declForStmt.
    def visitDeclForStmt(self, ctx:MiniDecafParser.DeclForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#forStmt.
    def visitForStmt(self, ctx:MiniDecafParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#whileStmt.
    def visitWhileStmt(self, ctx:MiniDecafParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MiniDecafParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#breakStmt.
    def visitBreakStmt(self, ctx:MiniDecafParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#continueStmt.
    def visitContinueStmt(self, ctx:MiniDecafParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#decl.
    def visitDecl(self, ctx:MiniDecafParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#expr.
    def visitExpr(self, ctx:MiniDecafParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tAsgn.
    def visitTAsgn(self, ctx:MiniDecafParser.TAsgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cAsgn.
    def visitCAsgn(self, ctx:MiniDecafParser.CAsgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tCond.
    def visitTCond(self, ctx:MiniDecafParser.TCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cCond.
    def visitCCond(self, ctx:MiniDecafParser.CCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cLor.
    def visitCLor(self, ctx:MiniDecafParser.CLorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tLor.
    def visitTLor(self, ctx:MiniDecafParser.TLorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cLand.
    def visitCLand(self, ctx:MiniDecafParser.CLandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tland.
    def visitTland(self, ctx:MiniDecafParser.TlandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tEq.
    def visitTEq(self, ctx:MiniDecafParser.TEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cEq.
    def visitCEq(self, ctx:MiniDecafParser.CEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#eqOp.
    def visitEqOp(self, ctx:MiniDecafParser.EqOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tRel.
    def visitTRel(self, ctx:MiniDecafParser.TRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cRel.
    def visitCRel(self, ctx:MiniDecafParser.CRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#relOp.
    def visitRelOp(self, ctx:MiniDecafParser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cAdd.
    def visitCAdd(self, ctx:MiniDecafParser.CAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tAdd.
    def visitTAdd(self, ctx:MiniDecafParser.TAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#addOp.
    def visitAddOp(self, ctx:MiniDecafParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tMul.
    def visitTMul(self, ctx:MiniDecafParser.TMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cMul.
    def visitCMul(self, ctx:MiniDecafParser.CMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cCast.
    def visitCCast(self, ctx:MiniDecafParser.CCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tCast.
    def visitTCast(self, ctx:MiniDecafParser.TCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#mulOp.
    def visitMulOp(self, ctx:MiniDecafParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tUnary.
    def visitTUnary(self, ctx:MiniDecafParser.TUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#cUnary.
    def visitCUnary(self, ctx:MiniDecafParser.CUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#array.
    def visitArray(self, ctx:MiniDecafParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#funcCall.
    def visitFuncCall(self, ctx:MiniDecafParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#tPostfix.
    def visitTPostfix(self, ctx:MiniDecafParser.TPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#argList.
    def visitArgList(self, ctx:MiniDecafParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#imme.
    def visitImme(self, ctx:MiniDecafParser.ImmeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#identifer.
    def visitIdentifer(self, ctx:MiniDecafParser.IdentiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#expression.
    def visitExpression(self, ctx:MiniDecafParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#unaryOp.
    def visitUnaryOp(self, ctx:MiniDecafParser.UnaryOpContext):
        return self.visitChildren(ctx)



del MiniDecafParser