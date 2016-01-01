class AST(object):

    @property
    def value(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.value == other.value


class BinOp(AST):

    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right

    def eval(self):
        raise NotImplementedError

    @property
    def value(self):
        return self.eval()


class AddOp(BinOp):
    def eval(self):
        return self.left.value + self.right.value


class SubOp(BinOp):
    def eval(self):
        return self.left.value - self.right.value


class MulOp(BinOp):
    def eval(self):
        return self.left.value * self.right.value


class DivOp(BinOp):
    def eval(self):
        return self.left.value / self.right.value


class Num(AST):

    def __init__(self, token):
        self.token = token

    @property
    def value(self):
        return self.token.value
