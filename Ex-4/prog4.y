%{
  int yylex();
  #define YYSTYPE double
  #include <stdio.h>
  #include <ctype.h>
%}

%token NUMBER
%left '+' '-'
%left '*' '/'
%right UMINUS

%%
lines:
  lines expr '\n' {printf("%g\n",$2);}
| lines '\n'
| /*empty*/
;
expr:
  expr '+' expr {$$=$1+$3;}
| expr '-' expr {$$=$1-$3;}
| expr '*' expr {$$=$1*$3;}
| expr '/' expr {$$=$1/$3;}
| '(' expr ')' {$$=$2;}
| '-' expr %prec UMINUS {$$=-$2;}
| NUMBER
;
%%
yylex(){
  int c;
  while((c=getchar())==' ');
  if(((c==' ')||(isdigit(c)))){
    ungetc(c,stdin);
    scanf("%lf",&yylval);
    return NUMBER;
  }
  return c;
}
int main()
{
  yyparse();
  return 0;
}
int yyerror(){
  printf("Syntax erorr! \n");
  return 1;
}
int yywrap()
{
  return 1;
}
