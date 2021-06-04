#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define n 500

void llenarMatriz(int **a);
void multiplicacion(int **a, int **b, int **c);
void imprimirMatriz (int **a);

main(){
    int **a,**b,**c,i;
    double empezar, terminar;
    printf("Multiplicacion de matrices en serie.\n");
    a = (int **)malloc(sizeof(int)*n);
    b = (int **)malloc(sizeof(int)*n);
    c = (int **)malloc(sizeof(int)*n);
    for(i=0; i<n; i++){ 
        a[i] = (int *)malloc(sizeof(int)*n);
        b[i] = (int *)malloc(sizeof(int)*n);
        c[i] = (int *)malloc(sizeof(int)*n);
    }

   llenarMatriz(a);
   llenarMatriz(b);
   
   
   empezar = omp_get_wtime();
   
   multiplicacion(a,b,c);
   
   terminar = omp_get_wtime();
   
   printf("El tiempo que tardo fue: %lf", terminar - empezar);
}

void llenarMatriz(int **a){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0; j<n; j++){
            a[i][j] = rand() % n;
        }
    }
}

void imprimirMatriz(int **a){
	int i,j;
	for (i = 0; i < n; i ++){
		for (j = 0; j < n; j++){
			printf("[%d] ",a[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void multiplicacion(int **a, int **b, int **c){
    int i,j,k;
    for (i = 0; i < n; i++){
        for(j = 0; j < n; j++){
        	c[i][j] = 0;
        	for (k = 0; k<n; k++){
        		c[i][j] += a[i][k] * b[k][j];
        	}
        }
    }
}
