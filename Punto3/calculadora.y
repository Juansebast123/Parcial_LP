%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int yylex(void);
void yyerror(char *s);
extern FILE *yyin;
%}

%union {
    float fval;
}

/* declare tokens */
%token <fval> NUMBER
%token ADD SUB MUL DIV ABS SQRT UMINUS
%token EOL

%type <fval> exp factor term

%start calclist

%%
calclist:
 | calclist exp EOL { printf("= %f\n", $2); }
 | EOL { }
 ;
exp: factor { $$ = $1; }
 | exp ADD factor { $$ = $1 + $3; }
 | exp SUB factor { $$ = $1 - $3; }
 ;
factor: term { $$ = $1; } 
 | factor MUL term { $$ = $1 * $3; }
 | factor DIV term { 
	if ($3 == 0.0f) { yyerror("division by zero"); $$ = 0.0; }
        else $$ = $1 / $3; }
 ;
term: NUMBER { $$ = $1; } 
 | '(' exp ')' { $$ = $2; }
 | SUB term %prec UMINUS { $$ = -$2; }
 | ABS term { $$ = $2 >= 0 ? $2 : -$2; }
 | SQRT term { 
        if ($2 < 0.0f) { yyerror("sqrt numero negativo"); $$ = 0.0; }
        else $$ = sqrt($2); }
;
%%
int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *f = fopen(argv[1], "r");
        if (!f) {
            perror("Error al abrir el archivo");
            return 1;
        }
        yyin = f;
    }
    return yyparse();
}

void yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s);
}

