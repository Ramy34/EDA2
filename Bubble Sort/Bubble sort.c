#include <stdio.h>

int main (){
	int a[] = {2,4,8,1,23,56,12,897,45};
	int i,temp,j;
	printf("\tBubble Sort\n");
	for (i=0;i<9;i++){
		for (j=0;j<9;j++){
			if(a[j] > a[j+1] ){
			temp = a[j];
			a[j] = a[j+1];
			a[j+1] = temp;
			}
		}
	}
	printf("De menor a mayor\n");
	for (i=0;i<9;i++){
		printf("Elemento %d : %d\n",(i+1),a[i]);
	}
	return 0;
}
