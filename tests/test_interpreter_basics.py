from pytest import raises

from Interpreter import Interpreter
from Token import Token, TokenTypes


def test_eat():
    i = Interpreter('1 2 + +')
    assert i.current_token == Token(TokenTypes.INT, 1)

    i.eat(TokenTypes.INT)
    assert i.current_token == Token(TokenTypes.INT, 2)

    i.eat(TokenTypes.INT)
    assert i.current_token == Token(TokenTypes.ADD)

    with raises(Exception):
        i.eat(TokenTypes.INT)


def test_invalid_token():
    with raises(Exception):
        Interpreter('$').run()


def test_factor():
    i = Interpreter('1 2')

    assert i.factor() == 1
    assert i.factor() == 2


def test_str_repr():
    i = Interpreter('1 + 2')

    assert str(i) == '<Interpreter <Lexer 1[ ]+ 2> <Token type=INT value=1>>'
    assert repr(i) == '<Interpreter <Lexer 1[ ]+ 2> <Token type=INT value=1>>'
