from TokenTypes import TokenTypes


class Token(object):

    def __init__(self, token_type, value=None):
        assert token_type in TokenTypes
        self.type = token_type
        self.value = value

    def __str__(self):
        return '<Token type={type}{value}>'.format(
            type=self.type,
            value=' value={}'.format(self.value) if self.value is not None else ''
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return \
            self.type == other.type and \
            self.value == other.value
