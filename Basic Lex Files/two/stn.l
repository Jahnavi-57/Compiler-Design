%{
#include <stdio.h>
int s,t,n=0;
%}

%%
[ ] {s++;}
[\t] {t++;}
[\n] {n++;}
%%

int main()
{
    yylex();
    printf("Spaces : %d, Tabs: %d, Newlines: %d\n", s,t,n);
}