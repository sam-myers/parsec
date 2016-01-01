class AST(object):
    pass


class BinOp(AST):

    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right


class Num(AST):

    def __init__(self, token):
        self.token = token
