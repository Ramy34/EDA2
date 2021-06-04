#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#define N 10 //1000
#define NG 10  //256

main(){
	double tej, empezar, terminar;
	
	int IMA[N][N], histo[NG], B[N],C[N];
	int i, j, tid, hmin, imin, spm=0, x;
	
	for (i = 0; i < N; i ++){
		for (j = 0; j < N; j ++){
			IMA[i][j] = rand() % 100;
		}
	}

	printf("\n Matriz IMA ");
	for (i = 0; i < 10; i ++){
		printf("\n");
		for(j = 0; j < 10; j ++)
			printf( "%3d ",IMA[i][j]);
		printf("\n");
	}

	for(i = 0; i < NG ;i ++)
		histo[i]=0;
	empezar = omp_get_wtime();

    int histop[NG];
	#pragma omp parallel private(j,histop)
	{
		for (j = 0; j < NG; j++){
			histop[i] = 0;
		}
		#pragma omp for
		for(i=0;i<N;i++)
		    for(j=0;j<N;j++)
			    histop[IMA[i][j]]++;
		#pragma omp critical
		{
			for (i = 0; i < NG; i++){
				histo[i] = histo[i] + histop[i];
			}
		}
	}
	
	hmin = N*N+1;
	#pragma omp parallel for
	for(i=0;i<NG;i++)
		if(hmin >histo[i]){
			#pragma omp critical
			{
			    if(hmin >histo[i]){
				    hmin=histo[i];
			        imin=i;	
			    }
			}
			
		}
	#pragma omp parallel for private(j,x) reduction(+:spm)
	for(i=0;i<N;i++){
		j=0;
		x=0;
		while((IMA[i][j]!=imin)&&(j<N)){
			x=x+IMA[i][j];
			j++;
		}
		B[i]=x;
		C[i]=j;
		spm=spm+j;
	}
	
	terminar = omp_get_wtime();

	printf("\n Histograma \n");
	for(i=0;i<10;i++)
	    printf("%5d",i);
	printf("\n");

	for(i=0;i<10;i++)
	    printf("%5d",histo[i]);
	printf("\n hmin= %d  imin = %d\n",hmin,imin);	
	
	printf("\n VectorB \n");
	for(i=0;i<10;i++)
		printf("%3d",B[i]);
	
	printf("\n Vector C\n");
	for(i=0;i<10;i++)
		printf("%3d",C[i]);
	
	printf("\n SPM = %d\n\n",spm);
	
	printf("Tiempo: %lf\n ",terminar - empezar);
} 
