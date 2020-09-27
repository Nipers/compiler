# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniDecafParser import MiniDecafParser
else:
    from MiniDecafParser import MiniDecafParser

# This class defines a complete generic visitor for a parse tree produced by MiniDecafParser.

class MiniDecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniDecafParser#function.
    def visitFunction(self, ctx:MiniDecafParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#returntype.
    def visitReturntype(self, ctx:MiniDecafParser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#main.
    def visitMain(self, ctx:MiniDecafParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#content.
    def visitContent(self, ctx:MiniDecafParser.ContentContext):
        return self.visitChildren(ctx)



del MiniDecafParser