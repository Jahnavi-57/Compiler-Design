%{
#include <stdio.h>
int d=0;
%}

%%
[0-9] {d++;}
%%

int yywrap(){
    return 1;
}

int main()
{
    printf("Enter the number..press ^d at end : \n");
    yylex();
    printf("No of digits present : %d \n",d);
}