grammar Gramatica;

prog: main;

main: 'Program' VARNAME '{' decVar* comandos+ '}';

decVar: varDecl | constDecl;
varDecl: VARTYPE VARNAME (',' VARNAME)* ';';
constDecl: 'const' VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL) (',' VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL))* ';';

comandos: comando+;

opMath: VARNAME '=' (expressao | expressaoBooleana) ';';

comando: funcinput
       | funcprint
       | opMath
       | condicional
       | cmdWhile
       | 'break' ';';

funcprint: 'print' '(' expressao (',' expressao)* ')' ';';
funcinput: 'input' '(' VARNAME (',' VARNAME)* ')' ';';

condicional
    : 'if' '(' expressaoBooleana ')' '{' comandos '}' ( 'else' '{' comandos '}' )?
    ;
cmdWhile: 'while' '(' expressaoBooleana ')' '{' comandos '}';


expressao: expressaoAritmetica | STRING;

expressaoAritmetica: termo (( '+' | '-' ) termo)*;

termo: fator (('*' | '/') fator)*;

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


WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' .*? '*/' -> skip;
