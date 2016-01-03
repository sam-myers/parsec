from Interpreter import Interpreter


def test_addition():
    assert Interpreter('1 + 3').run() == 4
    assert Interpreter('0 + 19').run() == 19
    assert Interpreter('7+7').run() == 14


def test_multi_part_addition():
    assert Interpreter('1 + 1 + 5').run() == 7


def test_subtraction():
    assert Interpreter('10 - 6').run() == 4
    assert Interpreter('0 - 2').run() == -2


def test_multi_part_subtraction():
    assert Interpreter('100 - 10 - 20').run() == 70


def test_multiplication():
    assert Interpreter('10 * 10').run() == 100


def test_multi_part_multiplication():
    assert Interpreter('2 * 2 * 2').run() == 8


def test_division():
    assert Interpreter('10 / 5').run() == 2


def test_multi_part_division():
    assert Interpreter('100 / 5 / 4').run() == 5


def test_precedence():
    assert Interpreter('3 * 5 + 2').run() == 17
    assert Interpreter('3 + 5 * 2').run() == 13
    assert Interpreter('14 + 2 * 3 - 6 / 2').run() == 17


def test_parenthesis():
    assert Interpreter(
            '7 + 3 * (10 / (12 / (3 + 1) - 1))'
    ).run() == 22

    assert Interpreter(
            '7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)'
    ).run() == 10


def test_negative_numbers():
    assert Interpreter('0 + -1').run() == -1
    assert Interpreter('10 * -7').run() == -70
