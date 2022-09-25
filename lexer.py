import sys
import ply.lex as lex 
import ply.yacc as yacc

reserved = {
    'programa' : 'PROGRAMA',
    'si' : 'COND_SI',
    'entonces':'ENTONCES',
    'sino' : 'COND_SINO',
    'mientras':'MIENTRAS',
    'para':'PARA',
    'clase':'CLASE',
    'imprime' : 'IMPRIME',
    'funcion':'FUNCION',
    'var' : 'VAR',
    'int' : 'INT',
    'float':'FLOAT',
    'string':'STRING',
    'bool':'BOOL',
    'char': 'CHAR',
    'verdadero':'VERDADERO',
    'falso':'FALSO',
    'regresa':'REGRESA',
    'fin':'FIN',
    'principal':'PRINCIPAL',
}

#tokens iniciales
tokens = [
    'MAS',
    'MENOS',
    'POR',
    'DIVIDE',
    'ID',
    'IGUAL',
    'MAYOR_QUE',
    'MENOR_QUE',
    'DIFERENTE_A',
    'LPARENT',
    'RPARENT',
    'LBRACE',
    'RBRACE',
    'CTEINT',
    'CTEFLOAT',
    'COMA',
    'SEMICOLON',
    'COLON',
    'STRING',
    'PUNTO',
    'CHAR'
] +list(reserved.values())

#expresiones regulares para tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDE = r'/'
t_IGUAL = r'\='
t_DIFERENTE_A = r'<>'
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMA = r','
t_PUNTO = r'\.'
t_SEMICOLON = r';'
t_COLON = r':'
t_CTEINT = r'[0-9]+'
t_CTEFLOAT = r'[0-9]+\.[0-9]+'
t_STRING = r'"([^\\"\n]+|\\.)*"'
t_CHAR = r"\'.\'"

#agregar palabras reservadas a los tokens
tokens = tokens + list(reserved.values())

#checa palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

#definir regla
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#ignorar espacios en blanco del archivo
t_ignore = r' '

#error 
def t_error(t):
    print("Error en caracter '%s'" % t.value[0])
    t.lexer.skip(1)

# construir analizador lexico
lex.lex()