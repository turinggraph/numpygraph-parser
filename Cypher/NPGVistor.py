__author__ = 'hp027'

from CypherVisitor import CypherVisitor
from CypherParser import CypherParser
import pdb

class NPGVisitor(CypherVisitor):
    def __init__(self):
        self.memory = {}

    def visitOC_Where(self, ctx):
        print("######", ctx, dir(ctx))
        print(ctx.SP())
        print(ctx.WHERE())
        # pdb.set_trace()
        print(ctx.oC_Expression())

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == CypherParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == CypherParser.ADD:
            return left + right
        return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
