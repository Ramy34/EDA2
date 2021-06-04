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
    int i, tid, inicio, fin;
    omp_set_num_threads(2);
    #pragma omp parallel private(inicio,fin,tid,i)
    {
        tid = omp_get_thread_num();
        inicio = tid * 5;
        fin = (tid + 1) * 5 - 1;
        for(i = inicio; i <= fin; i++){
            c[i] = a[i] + b[i];
            printf("hilo %d calculo c[%d] = %d\n",tid ,i ,c[i]);
        }
    }
}
