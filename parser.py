import ply.yacc as yacc
from re import U 
#Obtener tokens del lexer
from lexer import tokens
import sys 
#Data pretty printer
from pprint import pprint


OpStack = []

#Cuadruplos
Cuadruplos = []
#Hacer GOTO a main
Cuadruplos.append(["GOTO", " ", "main", " "])
#Pilas
PilaO = []
PilaSaltos = []
PilaTipos = []
PilaDimensiones =[]
PilaIDs = []

#"Cubo" Semantico
cubosemantico = {
    "int" : {
        "+": {
            "int" : "int",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        "-": {
            "int" : "int",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        "/": {
            "int" : "int",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        "*": {
            "int" : "int",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        ">": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "<": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "!=": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "==": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "=": {
            "int" : "int",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
    }, 
    "float" : {
        "+": {
            "int" : "float",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        "-": {
            "int" : "float",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        "/": {
            "int" : "float",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        "*": {
            "int" : "float",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },
        ">": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "<": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "!=": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "==": {
            "int" : "bool",
            "float" : "bool",
            "bool" : "error",
            "string" : "error"
        },
         "=": {
            "int" : "float",
            "float" : "float",
            "bool" : "error",
            "string" : "error"
        },

    },
    "string" : {
        "+": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "string"
        },
        "-": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        "/": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        "*": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        ">": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
         "<": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
         "!=": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "bool"
        },
         "==": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "bool"
        },
         "=": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "string"
        },
    },
     "bool" : {
        "+": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        "-": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        "/": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        "*": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
        ">": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
         "<": {
            "int" : "error",
            "float" : "error",
            "bool" : "error",
            "string" : "error"
        },
         "!=": {
            "int" : "error",
            "float" : "error",
            "bool" : "bool",
            "string" : "error"
        },
         "==": {
            "int" : "error",
            "float" : "error",
            "bool" : "bool",
            "string" : "error"
        },
         "=": {
            "int" : "error",
            "float" : "error",
            "bool" : "bool",
            "string" : "error"
        },
    },
}


#reglas gramaticales
def p_programa(p):
    ''' programa : PROGRAMA ID SEMICOLON main FIN
                | PROGRAMA ID SEMICOLON vars main FIN
    '''

def p_main(p):
 '''main : PRINCIPAL LPARENT RPARENT bloque'''

def p_vars(p):
    ''' vars : VAR vars2
    '''

def p_vars2(p):
    ''' vars2 : vars3 COLON tipo SEMICOLON vars2
                | vars3 COLON tipo SEMICOLON 
    '''

def p_vars3(p):
    ''' vars3 : ID
            | ID COMA vars3
    '''

def p_tipo(p):
    ''' tipo : INT
            | FLOAT
    '''

def p_bloque(p):
    ''' bloque : LBRACE estatuto2 RBRACE
                | LBRACE RBRACE
    '''

def p_estatuto2(p):
    ''' estatuto2 : estatuto
                | estatuto2 estatuto 
    '''

def p_estatuto(p):
    ''' estatuto : asignacion
                | condicion
                | escritura
    '''
def p_asignacion(p):
    ''' asignacion : ID IGUAL expresion SEMICOLON
    '''

def p_condicion(p):
    '''condicion : COND_SI LPARENT expresion RPARENT bloque SEMICOLON
                | COND_SI LPARENT expresion RPARENT bloque COND_SINO bloque SEMICOLON
    '''

def p_escritura(p):
    ''' escritura : IMPRIME LPARENT escrituraGrammar RPARENT SEMICOLON
    '''

def p_escrituraGrammar(p):
    ''' escrituraGrammar : expresion
                        | expresion COMA escrituraGrammar
                        | varcte
                        | varcte COMA escrituraGrammar
    '''

def p_expresion(p):
    ''' expresion : exp
                | exp MAYOR_QUE exp
                | exp MENOR_QUE exp
                | exp DIFERENTE_A exp
    '''

def p_exp(p):
    ''' exp : termino
            | termino exp2
    '''

def p_exp2(p):
    '''exp2 : MAS exp
            | MENOS exp
    '''

def p_termino(p):
    ''' termino : factor
            | factor termino2
    '''

def p_termino2(p):
    ''' termino2 : POR termino
                | DIVIDE termino
    '''

def p_factor(p):
    ''' factor : LPARENT expresion RPARENT
            | MAS varcte
            | MENOS varcte
            | varcte
    '''

def p_varcte(p):
    ''' varcte : ID
            | CTEFLOAT
            | CTEINT
            | STRING
    '''
def p_error(p):
    print("Error de sintaxis: '%s'" % p.value)
    sys.exit()

def p_vacio(p):
    '''vacio :'''
    p[0] = None


#crear parser
parser = yacc.yacc(debug = True) 
#verificar que el archivo existe
try:
    namef = "/Users/ivananguiano/Documents/Github/ProyectoAD2022/prueba.txt"
    file = open(namef,'r')
    s = file.read()
    file.close()
except EOFError:
    quit()
#parsear archivo
yacc.parse(s)
print("Apropiado")