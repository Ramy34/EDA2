#include<stdio.h>
#include<omp.h>

long fibonacci(int n);

main (){
	int nthr=0;
	int n;
	double empezar,terminar;
	long resul;
	empezar = omp_get_wtime();
	printf("\n Numero a calcular? ");
	scanf("%d", &n);
	resul = fibonacci(n);
	terminar = omp_get_wtime();
	printf ("\nEl numero Fibonacci de %5d es %d\n", n, resul);
	printf("El tiempo fue de: %lf\n",terminar - empezar);
}

long fibonacci(int n) {
	long fn1, fn2, fn;
	int id;
	if ( n == 0 || n == 1 )
		return(n);
	if ( n < 30 ){
		fn1 = fibonacci(n-1);
		fn2 = fibonacci(n-2);
		fn = fn1 + fn2;
	}
	return(fn);
}
