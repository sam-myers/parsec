from Parser import Parser


def test_addition():
    assert Parser('1 + 3').parse() == 4
    assert Parser('0 + 19').parse() == 19
    assert Parser('7+7').parse() == 14


def test_multi_part_addition():
    assert Parser('1 + 1 + 5').parse() == 7


def test_subtraction():
    assert Parser('10 - 6').parse() == 4
    assert Parser('0 - 2').parse() == -2


def test_multi_part_subtraction():
    assert Parser('100 - 10 - 20').parse() == 70


def test_multiplication():
    assert Parser('10 * 10').parse() == 100


def test_multi_part_multiplication():
    assert Parser('2 * 2 * 2').parse() == 8


def test_division():
    assert Parser('10 / 5').parse() == 2


def test_multi_part_division():
    assert Parser('100 / 5 / 4').parse() == 5


def test_precedence():
    assert Parser('3 * 5 + 2').parse() == 17
    assert Parser('3 + 5 * 2').parse() == 13
    assert Parser('14 + 2 * 3 - 6 / 2').parse() == 17


def test_parenthesis():
    assert Parser(
            '7 + 3 * (10 / (12 / (3 + 1) - 1))'
    ).parse() == 22

    assert Parser(
            '7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)'
    ).parse() == 10
