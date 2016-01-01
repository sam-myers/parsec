from pytest import raises

from AST import Num
from Parser import Parser
from Token import Token, TokenTypes


def test_eat():
    i = Parser('1 2 + +')
    assert i.current_token == Token(TokenTypes.INT, 1)

    i.eat(TokenTypes.INT)
    assert i.current_token == Token(TokenTypes.INT, 2)

    i.eat(TokenTypes.INT)
    assert i.current_token == Token(TokenTypes.ADD)

    with raises(Exception):
        i.eat(TokenTypes.INT)


def test_invalid_token():
    with raises(Exception):
        Parser('$').parse()


def test_factor():
    i = Parser('1 2')

    assert i.factor() == Num(Token(TokenTypes.INT, 1))
    assert i.factor() == Num(Token(TokenTypes.INT, 2))


def test_str_repr():
    i = Parser('1 + 2')

    assert str(i) == '<Interpreter <Lexer 1[ ]+ 2> <Token type=INT value=1>>'
    assert repr(i) == '<Interpreter <Lexer 1[ ]+ 2> <Token type=INT value=1>>'
