grammar Gramatica;

prog: main;

main: 'Program' VARNAME '{' decVar* comandos+ '}';

decVar: varDecl | constDecl;
varDecl: VARTYPE VARNAME (',' VARNAME)* ';';
constDecl: 'const' VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL) (',' VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL))* ';';

comandos: comando+;

comando: funcinput
       | funcprint
       | opMath
       | condicional
       | cmdWhile
       | 'break' ';';

funcprint: 'print' '(' expressao (',' expressao)* ')' ';';
funcinput: 'input' '(' VARNAME (',' VARNAME)* ')' ';';

condicional: 'if' '(' expressaoBooleana ')' '{' comandos '}' (ELSE '{' comandos '}')?;
cmdWhile: 'while' '(' expressaoBooleana ')' '{' comandos '}';

opMath: VARNAME '=' (expressaoAritmetica | expressaoBooleana) ';';

expressao: expressaoAritmetica | STRING;

expressaoAritmetica: termo ('+' termo | '-' termo)*;
termo: fator ('*' fator | '/' fator)*;
fator: VARNAME
     | VALFLOAT
     | VALINT
     | '(' expressaoAritmetica ')';

expressaoBooleana: expressaoAritmetica ( ('==' | '!=' | '<' | '<=' | '>' | '>=') expressaoAritmetica )?
                 | '!' expressaoBooleana
                 | VALBOOL
                 | '(' expressaoBooleana ')';

VARTYPE: 'int' | 'float' | 'bool' | 'str';
VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;
VALBOOL: 'true' | 'false';
VALINT: [0-9]+;
VALFLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
ELSE: 'else';

WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' .*? '*/' -> skip;
