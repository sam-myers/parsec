from enum import Enum


class TokenTypes(Enum):
    INT = 'INT'
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    L_PAREN = '('
    R_PAREN = ')'
    EOF = 'EOF'

    def __str__(self):
        return self.value
