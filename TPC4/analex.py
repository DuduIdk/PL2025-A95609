import re
import ply.lex as lex # type: ignore

tokens = {
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
}

t_SELECT = r'(?i:SELECT)'
t_WHERE = r'(?i:WHERE)'
t_LIMIT = r'(?i:LIMIT)'
t_DOT = r'\.'
t_LBRAC = r'\{'
t_RBRAC = r'\}'

def t_VAR(t):
    r'\?w+'
    t.value = t.value.strip('?')
    return t

t_A = r'a'
t_LANG= r'@[a-z]{2,3}([a-z]{2,3})'
t_PREF = r'[a-zA-Z][a-zA-Z]'


