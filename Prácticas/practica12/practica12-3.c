#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void llenarArreglo(double *a, int n);
double prodpunto (double *a, double *b, int n);

main(){
    int n = 10;
    double *a, *b,res = 0;
    a = (double *)malloc(sizeof(double)*n);
    b = (double *)malloc(sizeof(double)*n);
    llenarArreglo(a,n);
    llenarArreglo(b,n);
    res = prodpunto(a,b,n);
    printf("El resultado es: %g \n",res);
}

void llenarArreglo(double *a, int n){
    int i;
    for(i=0; i<n; i++){
        a[i] = rand() % n;
        printf("%g\t",a[i]);
    }
    printf("\n");
}

double prodpunto (double *a, double *b, int n){
    double res = 0;
    int i;
    #pragma omp parallel for reduction(+:res)
    for (i = 0; i < n; i++){
        res += a[i] * b[i];
    }
    return res;
}
