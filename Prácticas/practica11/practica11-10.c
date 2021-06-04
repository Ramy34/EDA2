#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define n 10

void llenarArreglo(int *a);
void suma(int *a, int *b, int *c);

main(){
    int max, *a, *b, *c;
    a = (int *)malloc(sizeof(int)*n);
    b = (int *)malloc(sizeof(int)*n);
    c = (int *)malloc(sizeof(int)*n);

    llenarArreglo(a);
    llenarArreglo(b);

    suma(a,b,c);
}

void llenarArreglo(int *a){
    int i;
    for(i=0; i<n; i++){
        a[i] = rand() % n;
        printf("%d\t",a[i]);
    }
    printf("\n");
}

void suma(int *a, int *b, int *c){
    int i, tid;
    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        #pragma omp for
        for(i = 0; i < n; i++){
            c[i] = a[i] + b[i];
            printf("hilo %d calculo c[%d] = %d\n",tid ,i ,c[i]);
        }
    }
}
