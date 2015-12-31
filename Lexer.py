import logging

from Token import Token
from TokenTypes import TokenTypes, TOKEN_DICT


class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0

        if len(source_code) == 0:
            self.current_character = None
            self.eof = True
        else:
            self.current_character = self.source_code[0]
            self.eof = False

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.eof:
            representation = '<Lexer EOF>'
        else:
            representation = '<Lexer {before}[{position}]{after}>'.format(
                before=self.source_code[:self.position],
                position=self.source_code[self.position],
                after=self.source_code[self.position+1:]
            )
        return representation

    def error(self, message):
        raise Exception(message)

    def advance(self):
        self.position += 1
        if self.position > len(self.source_code) - 1:
            self.current_character = ''
            self.eof = True
            self.position = len(self.source_code) - 1
            return
        self.current_character = self.source_code[self.position]

    def next_token(self):
        while not self.eof:

            if self.current_character in TOKEN_DICT:
                self.current_token = Token(
                    TOKEN_DICT[self.current_character]
                )
                self.advance()

            elif self.current_character.isspace():
                self.skip_whitespace()
                continue

            elif self.current_character.isdigit():
                self.current_token = Token(TokenTypes.INT, self.parse_integer())

            else:
                self.error('Unrecognized character: {token}'.format(
                    token=self.current_character
                ))
            logging.info('Parsed {}'.format(self.current_token))
            return self.current_token
        return Token(TokenTypes.EOF)

    def parse_integer(self):
        digits = ''
        while self.current_character.isdigit():
            digits += self.current_character
            self.advance()
        return int(digits)

    def skip_whitespace(self):
        while self.current_character is not None and self.current_character.isspace():
            self.advance()
