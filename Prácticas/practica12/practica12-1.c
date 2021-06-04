#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int buscaMaximo(int *a, int n);
void llenarArreglo(int *a, int n);

main(){
    int *a, max,n = 10;
    a = (int *)malloc(sizeof(int)*n);
    llenarArreglo(a,n);
    max = buscaMaximo(a,n);
    printf("El numero máximo es: %d \n",max);
}

void llenarArreglo(int *a, int n){
    int i;
    for(i=0; i<n; i++){
        a[i] = rand() % n;
        printf("%d\t",a[i]);
    }
    printf("\n");
}

int buscaMaximo(int *a, int m){
    int max,i;
    max = a[0];
    #pragma omp parallel for
    for(i = 1; i < m; i++){
        if(a[i] > max){
            #pragma omp critical
            {
                if(a[i] > max)
                max = a[i];
            }
         }
    }
    return max;
}
