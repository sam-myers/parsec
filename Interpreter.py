from NodeVisitor import NodeVisitor
from Parser import Parser
from TokenTypes import TokenTypes


class Interpreter(NodeVisitor):

    def __init__(self, source_code):
        self.parser = Parser(source_code)

    def run(self):
        ast = self.parser.parse()
        return self.visit(ast)

    def visit_Num(self, node):
        return node.token.value

    def visit_BinOp(self, node):
        if node.token.type == TokenTypes.ADD:
            return self.visit(node.left) + self.visit(node.right)

        elif node.token.type == TokenTypes.SUB:
            return self.visit(node.left) - self.visit(node.right)

        elif node.token.type == TokenTypes.MUL:
            return self.visit(node.left) * self.visit(node.right)

        elif node.token.type == TokenTypes.DIV:
            return self.visit(node.left) / self.visit(node.right)

        raise NotImplementedError
