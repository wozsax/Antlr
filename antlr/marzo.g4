grammar marzo;

program : expression+ ;

expression: 
    expression 'sum' expression         #suma
    | expression 'resta' expression     #resta 
    | Numero                            #primaria
    | Palabra                           #palabra
    | expression 'equals' expression    #igual
    | expression 'divide' expression    #dividir
    | expression 'times' expression     #multiplicar
    | expression 'less' expression      #menor
    | expression 'mayor' expression     #mayor
    ;

statement:
    'if' expression 'then' statement    #ifnoelse
    |'if' expression 'then' statement ('else' statement) ? #if
    |'imprimir' expression #print
    |'imNumber' Numero #declararNumero
    |'imWord'   Palabra #declararPalabra
;


// A continuación los tokens (comienzan con mayúscula)
Numero: [0-9]+;
Palabra: [a-zA-Z];
WS : [ \t\n\r]+ -> skip ;


