import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),
    ('IDENT',    r'[A-Za-z_][A-Za-z0-9_]*'),
    ('BOOL',     r'True|False'),
    ('STRING',   r'"[^"]*"'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MULT',     r'\*'),
    ('DIV',      r'/'),
    ('EQ',       r'='),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind in ['SKIP', 'NEWLINE']:
            continue
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'BOOL':
            value = True if value == 'True' else False
        elif kind == 'STRING':
            value = value.strip('"')
        tokens.append((kind, value))
    return tokens
