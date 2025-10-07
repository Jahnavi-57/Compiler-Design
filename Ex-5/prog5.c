#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void main(){
    char expr[50],c;
    void *addr[20],*p;
    int i=0,j=0,x=0;

    printf("Enter the expression ending with $ symbol\n");
    while((c=getchar())!='$'){
        expr[i++]=c;
    }
    printf("Symbol\taddress\t\tType\n");
    for(j=0;j<i;j++)
    {
        c=expr[j];
        if(isalpha(c))
        {
            p=malloc(1);
            addr[x++]=p;
            printf("%c\t%p\tIdentifier\n",c,p);
        }
        else if(c=='+'||c=='-'||c=='*'||c=='=')
        {
            p=malloc(1);
            addr[x++]=p;
            printf("%c\t%p\tOperator\n",c,p);
        }
    }
}