import re

# Token specifications
TOKEN_SPEC = [
    ('NUMBER',    r'\d+'),
    ('IDENT',     r'[a-zA-Z_]\w*'),
    ('ASSIGN',    r'='),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('MULT',      r'\*'),
    ('DIV',       r'/'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('PRINT',     r'print'),
    ('SKIP',      r'[ \t]+'),
    ('NEWLINE',   r'\n'),
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f'Token({self.type},{self.value})'

def tokenize(code):
    tokens = []
    for mo in re.finditer(TOKEN_REGEX, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        tokens.append(Token(kind, value))
    return tokens

# Recursive descent parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def expect(self, token_type):
        token = self.peek()
        if token and token.type == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {token_type} but got {token}")

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.statement())
        return statements

    def statement(self):
        token = self.peek()
        if token.type == 'IDENT':
            return self.assignment()
        elif token.type == 'PRINT':
            return self.print_stmt()
        else:
            raise SyntaxError(f"Unexpected token {token}")

    def assignment(self):
        ident = self.expect('IDENT').value
        self.expect('ASSIGN')
        expr = self.expr()
        return ('assign', ident, expr)

    def print_stmt(self):
        self.expect('PRINT')
        self.expect('LPAREN')
        expr = self.expr()
        self.expect('RPAREN')
        return ('print', expr)

    def expr(self):
        node = self.term()
        while self.peek() and self.peek().type in ('PLUS', 'MINUS'):
            op = self.expect(self.peek().type).type
            right = self.term()
            node = (op.lower(), node, right)
        return node

    def term(self):
        node = self.factor()
        while self.peek() and self.peek().type in ('MULT', 'DIV'):
            op = self.expect(self.peek().type).type
            right = self.factor()
            node = (op.lower(), node, right)
        return node

    def factor(self):
        token = self.peek()
        if token.type == 'NUMBER':
            self.expect('NUMBER')
            return ('num', int(token.value))
        elif token.type == 'IDENT':
            self.expect('IDENT')
            return ('var', token.value)
        elif token.type == 'LPAREN':
            self.expect('LPAREN')
            node = self.expr()
            self.expect('RPAREN')
            return node
        else:
            raise SyntaxError(f"Unexpected token in factor: {token}")

# Interpreter
class Interpreter:
    def __init__(self):
        self.vars = {}

    def eval(self, node):
        kind = node[0]
        if kind == 'num':
            return node[1]
        elif kind == 'var':
            return self.vars.get(node[1], 0)
        elif kind in ('plus', 'minus', 'mult', 'div'):
            left = self.eval(node[1])
            right = self.eval(node[2])
            if kind == 'plus':
                return left + right
            elif kind == 'minus':
                return left - right
            elif kind == 'mult':
                return left * right
            elif kind == 'div':
                return left // right  # integer division
        else:
            raise RuntimeError(f"Unknown expression {node}")

    def execute(self, stmt):
        op = stmt[0]
        if op == 'assign':
            self.vars[stmt[1]] = self.eval(stmt[2])
        elif op == 'print':
            print(self.eval(stmt[1]))
        else:
            raise RuntimeError(f"Unknown statement {stmt}")

    def run(self, statements):
        for stmt in statements:
            self.execute(stmt)

# Example usage
if __name__ == '__main__':
    code = """
    let x = 10
    let y = 20
    let z = x + y * 2
    print(z)
    """

    # Remove 'let' keywords if your language uses them (optional step)
    code = code.replace('let ', '')

    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    interpreter.run(ast)
