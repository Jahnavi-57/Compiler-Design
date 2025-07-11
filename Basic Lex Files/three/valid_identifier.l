%{
#include <stdio.h>
%}

%%
[a-zA-Z_][a-zA-Z0-9_]*\n {printf("Valid Identifier\n");}
.+\n {printf("Invalid Identifier\n");}
\n {printf("Invalid Identifier\n");}
%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the identifier : \n");
    yylex();
}