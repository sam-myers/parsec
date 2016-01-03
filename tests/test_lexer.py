from pytest import raises

from Lexer import Lexer
from Token import Token, TokenTypes


def test_repr():
    assert repr(Lexer('1 + 3')) == '<Lexer [1] + 3>'


def test_advance():
    lexer = Lexer('1 + 3')

    lexer.advance()
    assert repr(lexer) == '<Lexer 1[ ]+ 3>'

    lexer.advance()
    assert repr(lexer) == '<Lexer 1 [+] 3>'

    lexer.advance()
    assert repr(lexer) == '<Lexer 1 +[ ]3>'

    lexer.advance()
    assert repr(lexer) == '<Lexer 1 + [3]>'

    lexer.advance()
    assert repr(lexer) == '<Lexer EOF>'


def test_peek():
    lexer = Lexer('1 + 3')

    assert lexer.peek() == ' '
    lexer.advance()

    assert lexer.peek() == '+'
    lexer.advance()

    assert lexer.peek() == ' '
    lexer.advance()

    assert lexer.peek() == '3'
    lexer.advance()

    assert lexer.peek() is None
    lexer.advance()


def test_next_token():
    lexer = Lexer('1+ 3')

    assert lexer.next_token() == Token(TokenTypes.INT, 1)
    assert lexer.next_token() == Token(TokenTypes.ADD)
    assert lexer.next_token() == Token(TokenTypes.INT, 3)
    assert lexer.next_token() == Token(TokenTypes.EOF)


def test_empty_program():
    lexer = Lexer('')

    assert repr(lexer) == '<Lexer EOF>'
    assert lexer.next_token() == Token(TokenTypes.EOF)


def test_bad_input():
    lexer = Lexer('&')

    with raises(Exception):
        lexer.next_token()


def test_parse_integer():
    assert Lexer('173').next_token() == Token(TokenTypes.INT, 173)


def test_skip_whitespace():
    lexer = Lexer('1   +3 9')

    assert lexer.next_token() == Token(TokenTypes.INT, 1)
    assert lexer.next_token() == Token(TokenTypes.ADD)
    assert lexer.next_token() == Token(TokenTypes.INT, 3)
    assert lexer.next_token() == Token(TokenTypes.INT, 9)
    assert lexer.next_token() == Token(TokenTypes.EOF)


def test_math_symbols():
    lexer = Lexer('+ - * /')

    assert lexer.next_token() == Token(TokenTypes.ADD)
    assert lexer.next_token() == Token(TokenTypes.SUB)
    assert lexer.next_token() == Token(TokenTypes.MUL)
    assert lexer.next_token() == Token(TokenTypes.DIV)


def test_negative_numbers():
    lexer = Lexer('-3 * -2')

    assert lexer.next_token() == Token(TokenTypes.INT, -3)
    assert lexer.next_token() == Token(TokenTypes.MUL)
    assert lexer.next_token() == Token(TokenTypes.INT, -2)
