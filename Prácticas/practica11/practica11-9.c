#include <stdio.h>
int main(){
    #pragma omp parallel
    {
        int i;
        printf("Hola Mundo\n");
        #pragma omp for
            for(i = 0; i < 10; i++)
                printf("Iteracion:%d\n",i);
    }
    return 0;
}
