import re
import ply.lex as lex # type: ignore

string = """
#DBPedia: obras de Chuck Berry

SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en.
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc.
} LIMIT 1000
"""

tokens = [
    'SELECT',
    'WHERE',
    'LIMIT',
    'LBRAC',
    'RBRAC',
    'COMMENT',
    'VAR',
    'A',
    'DOT',
    'LANG',
    'INT',
    'STRING',
    'PREF'
]

t_SELECT = r'(?i:SELECT)'
t_WHERE = r'(?i:WHERE)'
t_LIMIT = r'(?i:LIMIT)'
t_DOT = r'\.'
t_LBRAC = r'\{'
t_RBRAC = r'\}'

def t_VAR(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value[1:]
    return t

def t_A(t):
    r'\ba\b'
    return t

t_LANG = r'@[a-z]{2,3}(-[a-z]{2,3})?'
t_PREF = r'[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z_][a-zA-Z0-9_-]*'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^"\\]*(\\.[^"\\]*)*)\"'
    t.value = t.value[1:-1]
    return t

t_COMMENT = r'\#.*'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(string)

for tok in lexer:
    print(tok.type, tok.value)
