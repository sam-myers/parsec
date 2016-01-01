from AST import BinOp, Num
from Lexer import Lexer
from TokenTypes import TokenTypes


class Parser(object):

    def __init__(self, source_code):
        self.lexer = Lexer(source_code)
        self.current_token = self.lexer.next_token()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<Parser {lexer} {token}>'.format(
            lexer=self.lexer,
            token=self.lexer.current_token
        )

    def error(self, message):
        raise Exception(message)

    def eat(self, token_type):
        if self.current_token.type != token_type:
            self.error('Attempted to eat {expected} but found {actual}'.format(
                expected=token_type,
                actual=self.current_token
            ))
        self.current_token = self.lexer.next_token()

    def parse(self):
        """Returns the complete Abstract Syntax Tree"""
        return self.expression()

    def expression(self):
        """expression: term ((ADD | SUB) term)*"""
        node = self.term()

        while self.lexer.current_token.type in (
            TokenTypes.ADD,
            TokenTypes.SUB
        ):
            current_token = self.lexer.current_token

            if current_token.type == TokenTypes.ADD:
                self.eat(TokenTypes.ADD)
                node = BinOp(node, current_token, self.term())

            elif current_token.type == TokenTypes.SUB:
                self.eat(TokenTypes.SUB)
                node = BinOp(node, current_token, self.term())

        return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.lexer.current_token.type in (
            TokenTypes.MUL,
            TokenTypes.DIV
        ):
            current_token = self.lexer.current_token

            if current_token.type == TokenTypes.MUL:
                self.eat(TokenTypes.MUL)
                node = BinOp(node, current_token, self.factor())

            elif current_token.type == TokenTypes.DIV:
                self.eat(TokenTypes.DIV)
                node = BinOp(node, current_token, self.factor())

        return node

    def factor(self):
        """factor : INTEGER | L_PAREN expression R_PAREN"""
        token = self.current_token

        if token.type == TokenTypes.INT:
            self.eat(TokenTypes.INT)
            node = Num(token)

        elif token.type == TokenTypes.L_PAREN:
            self.eat(TokenTypes.L_PAREN)
            node = self.expression()
            self.eat(TokenTypes.R_PAREN)

        return node
