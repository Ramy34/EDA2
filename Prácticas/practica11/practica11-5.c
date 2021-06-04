#include <stdio.h>
int main(){
    int i;
    #pragma omp parallel private(i)
    {
        printf("Hola Mundo\n");
        for(i = 0; i < 10; i++)
            printf("Iteracion:%d\n",i);
    }
    printf("Adiós\n");
return 0;
}
