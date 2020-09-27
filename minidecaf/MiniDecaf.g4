grammar MiniDecaf;

import CommonLex;

function: returntype main;
returntype: 'int';
main: 'main' Lparen Rparen Lbrace content Rbrace;
content: 'return' Integer;
