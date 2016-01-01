from pytest import raises

from AST import *
from Token import Token, TokenTypes


def test_abstract_ast_class():
    ast = AST()

    with raises(NotImplementedError):
        ast.value


def test_abstract_binop_class():
    ast = BinOp(None, None, None)

    with raises(NotImplementedError):
        ast.eval()


def test_ast_equal():
    assert Num(Token(TokenTypes.INT, 1)) == Num(Token(TokenTypes.INT, 1))
