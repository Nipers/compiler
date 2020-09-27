# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniDecafParser import MiniDecafParser
else:
    from MiniDecafParser import MiniDecafParser

# This class defines a complete listener for a parse tree produced by MiniDecafParser.
class MiniDecafListener(ParseTreeListener):

    # Enter a parse tree produced by MiniDecafParser#function.
    def enterFunction(self, ctx:MiniDecafParser.FunctionContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#function.
    def exitFunction(self, ctx:MiniDecafParser.FunctionContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#returntype.
    def enterReturntype(self, ctx:MiniDecafParser.ReturntypeContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#returntype.
    def exitReturntype(self, ctx:MiniDecafParser.ReturntypeContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#main.
    def enterMain(self, ctx:MiniDecafParser.MainContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#main.
    def exitMain(self, ctx:MiniDecafParser.MainContext):
        pass


    # Enter a parse tree produced by MiniDecafParser#content.
    def enterContent(self, ctx:MiniDecafParser.ContentContext):
        pass

    # Exit a parse tree produced by MiniDecafParser#content.
    def exitContent(self, ctx:MiniDecafParser.ContentContext):
        pass



del MiniDecafParser