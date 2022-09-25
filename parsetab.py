
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\t\x96"xG\xf0\x88y\xc4!)\xdbR\xf3\x86\xcf'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,9,15,],[0,-1,-2,]),'ID':([2,8,18,20,25,27,28,29,30,34,36,37,38,39,46,47,49,57,58,59,60,62,63,65,66,72,73,83,86,89,],[3,14,14,31,31,-13,-15,-16,-17,14,-14,41,41,41,41,41,41,-18,41,41,41,41,41,41,41,41,41,-21,-19,-20,]),'SEMICOLON':([3,21,22,23,26,35,41,42,43,44,45,48,50,51,52,61,64,68,69,71,74,75,76,77,78,79,80,81,82,88,],[4,34,-9,-10,-12,-11,-42,57,-26,-30,-34,-41,-43,-44,-45,-31,-35,-39,-40,83,-27,-28,-29,-32,-33,-36,-37,-38,86,89,]),'PRINCIPAL':([4,6,12,34,40,],[7,7,-4,-6,-5,]),'VAR':([4,],[8,]),'FIN':([5,10,19,26,35,],[9,15,-3,-12,-11,]),'LPARENT':([7,32,33,37,38,39,46,58,59,60,62,63,65,66,72,73,],[11,38,39,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'RPARENT':([11,41,43,44,45,48,50,51,52,53,54,55,56,61,64,67,68,69,74,75,76,77,78,79,80,81,84,85,],[16,-42,-26,-30,-34,-41,-43,-44,-45,70,71,-22,-24,-31,-35,81,-39,-40,-27,-28,-29,-32,-33,-36,-37,-38,-23,-25,]),'COLON':([13,14,24,],[17,-7,-8,]),'COMA':([14,41,43,44,45,48,50,51,52,55,56,61,64,68,69,74,75,76,77,78,79,80,81,],[18,-42,-26,-30,-34,-41,-43,-44,-45,72,73,-31,-35,-39,-40,-27,-28,-29,-32,-33,-36,-37,-38,]),'LBRACE':([16,70,87,],[20,20,20,]),'INT':([17,],[22,]),'FLOAT':([17,],[23,]),'RBRACE':([20,25,27,28,29,30,36,57,83,86,89,],[26,35,-13,-15,-16,-17,-14,-18,-21,-19,-20,]),'COND_SI':([20,25,27,28,29,30,36,57,83,86,89,],[32,32,-13,-15,-16,-17,-14,-18,-21,-19,-20,]),'IMPRIME':([20,25,27,28,29,30,36,57,83,86,89,],[33,33,-13,-15,-16,-17,-14,-18,-21,-19,-20,]),'COND_SINO':([26,35,82,],[-12,-11,87,]),'IGUAL':([31,],[37,]),'MAS':([37,38,39,41,44,45,46,48,50,51,52,56,58,59,60,62,63,64,65,66,68,69,72,73,79,80,81,],[47,47,47,-42,62,-34,47,-41,-43,-44,-45,-41,47,47,47,47,47,-35,47,47,-39,-40,47,47,-36,-37,-38,]),'MENOS':([37,38,39,41,44,45,46,48,50,51,52,56,58,59,60,62,63,64,65,66,68,69,72,73,79,80,81,],[49,49,49,-42,63,-34,49,-41,-43,-44,-45,-41,49,49,49,49,49,-35,49,49,-39,-40,49,49,-36,-37,-38,]),'CTEFLOAT':([37,38,39,46,47,49,58,59,60,62,63,65,66,72,73,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'CTEINT':([37,38,39,46,47,49,58,59,60,62,63,65,66,72,73,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'STRING':([37,38,39,46,47,49,58,59,60,62,63,65,66,72,73,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'POR':([41,45,48,50,51,52,56,68,69,81,],[-42,65,-41,-43,-44,-45,-41,-39,-40,-38,]),'DIVIDE':([41,45,48,50,51,52,56,68,69,81,],[-42,66,-41,-43,-44,-45,-41,-39,-40,-38,]),'MAYOR_QUE':([41,43,44,45,48,50,51,52,56,61,64,68,69,77,78,79,80,81,],[-42,58,-30,-34,-41,-43,-44,-45,-41,-31,-35,-39,-40,-32,-33,-36,-37,-38,]),'MENOR_QUE':([41,43,44,45,48,50,51,52,56,61,64,68,69,77,78,79,80,81,],[-42,59,-30,-34,-41,-43,-44,-45,-41,-31,-35,-39,-40,-32,-33,-36,-37,-38,]),'DIFERENTE_A':([41,43,44,45,48,50,51,52,56,61,64,68,69,77,78,79,80,81,],[-42,60,-30,-34,-41,-43,-44,-45,-41,-31,-35,-39,-40,-32,-33,-36,-37,-38,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'main':([4,6,],[5,10,]),'vars':([4,],[6,]),'vars2':([8,34,],[12,40,]),'vars3':([8,18,34,],[13,24,13,]),'bloque':([16,70,87,],[19,82,88,]),'tipo':([17,],[21,]),'estatuto2':([20,],[25,]),'estatuto':([20,25,],[27,36,]),'asignacion':([20,25,],[28,28,]),'condicion':([20,25,],[29,29,]),'escritura':([20,25,],[30,30,]),'expresion':([37,38,39,46,72,73,],[42,53,55,67,55,55,]),'exp':([37,38,39,46,58,59,60,62,63,72,73,],[43,43,43,43,74,75,76,77,78,43,43,]),'termino':([37,38,39,46,58,59,60,62,63,65,66,72,73,],[44,44,44,44,44,44,44,44,44,79,80,44,44,]),'factor':([37,38,39,46,58,59,60,62,63,65,66,72,73,],[45,45,45,45,45,45,45,45,45,45,45,45,45,]),'varcte':([37,38,39,46,47,49,58,59,60,62,63,65,66,72,73,],[48,48,56,48,68,69,48,48,48,48,48,48,48,56,56,]),'escrituraGrammar':([39,72,73,],[54,84,85,]),'exp2':([44,],[61,]),'termino2':([45,],[64,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA ID SEMICOLON main FIN','programa',5,'p_programa','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',255),
  ('programa -> PROGRAMA ID SEMICOLON vars main FIN','programa',6,'p_programa','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',256),
  ('main -> PRINCIPAL LPARENT RPARENT bloque','main',4,'p_main','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',260),
  ('vars -> VAR vars2','vars',2,'p_vars','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',263),
  ('vars2 -> vars3 COLON tipo SEMICOLON vars2','vars2',5,'p_vars2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',267),
  ('vars2 -> vars3 COLON tipo SEMICOLON','vars2',4,'p_vars2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',268),
  ('vars3 -> ID','vars3',1,'p_vars3','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',272),
  ('vars3 -> ID COMA vars3','vars3',3,'p_vars3','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',273),
  ('tipo -> INT','tipo',1,'p_tipo','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',277),
  ('tipo -> FLOAT','tipo',1,'p_tipo','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',278),
  ('bloque -> LBRACE estatuto2 RBRACE','bloque',3,'p_bloque','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',282),
  ('bloque -> LBRACE RBRACE','bloque',2,'p_bloque','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',283),
  ('estatuto2 -> estatuto','estatuto2',1,'p_estatuto2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',287),
  ('estatuto2 -> estatuto2 estatuto','estatuto2',2,'p_estatuto2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',288),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',292),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',293),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',294),
  ('asignacion -> ID IGUAL expresion SEMICOLON','asignacion',4,'p_asignacion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',297),
  ('condicion -> COND_SI LPARENT expresion RPARENT bloque SEMICOLON','condicion',6,'p_condicion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',301),
  ('condicion -> COND_SI LPARENT expresion RPARENT bloque COND_SINO bloque SEMICOLON','condicion',8,'p_condicion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',302),
  ('escritura -> IMPRIME LPARENT escrituraGrammar RPARENT SEMICOLON','escritura',5,'p_escritura','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',306),
  ('escrituraGrammar -> expresion','escrituraGrammar',1,'p_escrituraGrammar','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',310),
  ('escrituraGrammar -> expresion COMA escrituraGrammar','escrituraGrammar',3,'p_escrituraGrammar','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',311),
  ('escrituraGrammar -> varcte','escrituraGrammar',1,'p_escrituraGrammar','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',312),
  ('escrituraGrammar -> varcte COMA escrituraGrammar','escrituraGrammar',3,'p_escrituraGrammar','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',313),
  ('expresion -> exp','expresion',1,'p_expresion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',317),
  ('expresion -> exp MAYOR_QUE exp','expresion',3,'p_expresion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',318),
  ('expresion -> exp MENOR_QUE exp','expresion',3,'p_expresion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',319),
  ('expresion -> exp DIFERENTE_A exp','expresion',3,'p_expresion','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',320),
  ('exp -> termino','exp',1,'p_exp','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',324),
  ('exp -> termino exp2','exp',2,'p_exp','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',325),
  ('exp2 -> MAS exp','exp2',2,'p_exp2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',329),
  ('exp2 -> MENOS exp','exp2',2,'p_exp2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',330),
  ('termino -> factor','termino',1,'p_termino','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',334),
  ('termino -> factor termino2','termino',2,'p_termino','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',335),
  ('termino2 -> POR termino','termino2',2,'p_termino2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',339),
  ('termino2 -> DIVIDE termino','termino2',2,'p_termino2','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',340),
  ('factor -> LPARENT expresion RPARENT','factor',3,'p_factor','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',344),
  ('factor -> MAS varcte','factor',2,'p_factor','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',345),
  ('factor -> MENOS varcte','factor',2,'p_factor','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',346),
  ('factor -> varcte','factor',1,'p_factor','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',347),
  ('varcte -> ID','varcte',1,'p_varcte','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',351),
  ('varcte -> CTEFLOAT','varcte',1,'p_varcte','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',352),
  ('varcte -> CTEINT','varcte',1,'p_varcte','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',353),
  ('varcte -> STRING','varcte',1,'p_varcte','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',354),
  ('vacio -> <empty>','vacio',0,'p_vacio','/Users/ivananguiano/Documents/GitHub/ProyectoAD2022/parser.py',361),
]
