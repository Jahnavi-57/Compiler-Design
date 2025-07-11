%{
#include <stdio.h>
%}

%%
[a-z] {putchar(yytext[0]-32);}
.|\n {putchar(yytext[0]);}
%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the String : \n");
    yylex();
}