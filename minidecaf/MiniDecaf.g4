grammar MiniDecaf;

import CommonLex;

prog
    : content+ EOF
    ;

content
    : function #func
    | decl Semicolon# global
    ;
    
function
    : tp Ident Lparen paramList Rparen compound # funcDef
    | tp Ident Lparen paramList Rparen Semicolon # funcDecl
    ;

tp  
    : Int #intType
    | tp Asterisk # pointer
    ;

paramList
    : (decl (Comma decl)*)?
    ;

blockitem
    : stmt
    | decl Semicolon
    ;

compound
    : Lbrace blockitem* Rbrace
    ;

stmt
    : Return expr Semicolon #retStmt
    | expr Semicolon # exprStmt
    | Semicolon #voidStmt
    | If Lparen expr Rparen then=stmt (Else els = stmt)?#ifStmt
    | compound #cpdStmt
    | For Lparen init=decl Semicolon (ctrl=expr)?Semicolon(post=expr)?Rparen stmt #declForStmt
    | For Lparen (init=expr)?Semicolon(ctrl=expr)?Semicolon(post=expr)?Rparen stmt #forStmt
    | While Lparen expr Rparen stmt #whileStmt
    | Do stmt While Lparen expr Rparen Semicolon#doWhileStmt
    | Break Semicolon#breakStmt
    | Continue Semicolon#continueStmt 
    ;

decl
    : tp Ident (Lbrkt Integer Rbrkt)* (Equal expr)? 
    ;

expr
    : asgn
    ;

asgn
    : cond # tAsgn
    | unary Equal asgn # cAsgn
    ;

cond
    : lor # tCond
    | lor '?' expr ':' cond # cCond
    ;

lor
    : land # tLor
    | lor Double_bar land # cLor
    ;

land
    : eq # tland
    | land Double_amp eq #cLand
    ;

eq  
    : rel # tEq
    | eq eqOp rel # cEq
    ;

eqOp 
    : Double_eq | Exclam_eq
    ;

rel
    : add # tRel
    | rel relOp add # cRel
    ;

relOp
    : Langle|Rangle|Langle_eq|Rangle_eq
    ;

add
    : mul # tAdd
    | add addOp mul # cAdd
    ;
    
addOp
    : Plus | Minus
    ;

mul
    : cast #tMul
    | mul mulOp cast # cMul
    ;

cast
    : Lparen tp Rparen cast #cCast
    | unary #tCast
    ;

mulOp
    : Asterisk|Slash|Percent
    ;

unary
    : postfix #tUnary
    | unaryOp cast #cUnary
    ;

postfix
    : prim #tPostfix
    | postfix Lbrkt expr Rbrkt # array
    | Ident Lparen argList Rparen #funcCall
    ;

argList
    : (expr (Comma expr)*)?
    ;

prim    
    : Integer # imme
    | Ident # identifer
    | Lparen expr Rparen # expression
    ;

unaryOp
    : Minus | Exclamation | Tilde | Asterisk | Ampersand
    ;
