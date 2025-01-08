grammar Gramatica;

prog: main;

main: 'Program' VARNAME '{' decVar* comandos* '}';

decVar: 'const' consts ';' | 'var' ':' varlist+;
varlist: (VARNAME ','?)+ ':' VARTYPE ';';
consts: (VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL) ','?)+;

comandos: funcinput
        | funcprint
        | opMath
        | condicional
        | cmdWhile;

funcprint: 'print' '(' expressaoAritmetica (',' expressaoAritmetica)* ')' ';';
funcinput: 'input' '(' VARNAME (',' VARNAME)* ')' ';';

condicional: 'if' '(' expressaoBooleana ')' '{' comandos* '}' ('else' '{' comandos* '}')?;
cmdWhile: 'while' '(' expressaoBooleana ')' '{' comandos* '}';

opMath: VARNAME '=' (expressaoAritmetica | expressaoBooleana) ';';

expressaoAritmetica
    : termo ('+' termo | '-' termo)*
    ;
termo
    : fator ('*' fator | '/' fator)*
    ;
fator
    : VARNAME
    | VALFLOAT
    | VALINT
    | '(' expressaoAritmetica ')'
    ;

expressaoBooleana
    : expressaoAritmetica ( ('==' | '!=' | '<' | '<=' | '>' | '>=') expressaoAritmetica )?
    | '!' expressaoBooleana
    | VALBOOL
    | '(' expressaoBooleana ')'
    ;

VARTYPE: 'int' | 'float' | 'bool' | 'str';
VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;
VALBOOL: 'true' | 'false';
VALINT: [0-9]+;
VALFLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';

WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
COMMENT: '/*' .*? '*/' -> skip;
