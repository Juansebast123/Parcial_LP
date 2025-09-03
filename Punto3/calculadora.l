%{
#include "calculadora.tab.h"
%}

FLOAT   [0-9]+\.[0-9]+
INT     [0-9]+

%%
{FLOAT} { yylval.fval = atof(yytext); return NUMBER; }
{INT}   { yylval.fval = atof(yytext); return NUMBER; }
"+"     { return ADD; }
"-"     { return SUB; }
"*"     { return MUL; }
"/"     { return DIV; }
"("     { return '('; }
")"     { return ')'; }
"abs"   { return ABS; }
"sqrt"  { return SQRT; }
\n      { return EOL; }
[ \t]   { }
"//".*  { }
.       { return yytext[0]; }
%%

int yywrap() { return 1; }

