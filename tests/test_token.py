from Token import Token, TokenTypes


def test_create_int():
    i = Token(TokenTypes.INT, 7)

    assert i.type == TokenTypes.INT
    assert i.value == 7


def test_create_add():
    i = Token(TokenTypes.INT)

    assert i.type == TokenTypes.INT
    assert i.value is None


def test_create_sub():
    i = Token(TokenTypes.INT)

    assert i.type == TokenTypes.INT
    assert i.value is None


def test_create_mul():
    i = Token(TokenTypes.MUL)

    assert i.type == TokenTypes.MUL
    assert i.value is None


def test_create_div():
    i = Token(TokenTypes.DIV)

    assert i.type == TokenTypes.DIV
    assert i.value is None


def test_create_eof():
    i = Token(TokenTypes.EOF)

    assert i.type == TokenTypes.EOF


def test_equality_int():
    assert Token(TokenTypes.INT, 1) == Token(TokenTypes.INT, 1)


def test_inequality_int():
    assert Token(TokenTypes.INT, 1) != Token(TokenTypes.INT, 2)


def test_equality_eof():
    assert Token(TokenTypes.EOF) == Token(TokenTypes.EOF)


def test_repr_int():
    assert repr(Token(TokenTypes.INT, 1)) == '<Token type=INT value=1>'


def test_repr_eof():
    assert repr(Token(TokenTypes.EOF)) == '<Token type=EOF>'
