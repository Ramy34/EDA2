#include <stdio.h>
#include <omp.h>
int main(){
    //omp_set_num_threads(5);
    #pragma omp parallel num_threads(6)
    {
        int i;
        printf("Hola Mundo\n");
        for(i = 0; i < 10; i++)
            printf("Iteracion:%d\n",i);
    }
    printf("Adiós\n");
return 0;
}
