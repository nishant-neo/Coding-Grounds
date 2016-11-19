#include <stdio.h>

int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}
int main()
{
	int k, l ,r;
	int arr[] = { 2,6,3,5,32,3,1,9};
	int n = 8;
	qsort( arr, 8, sizeof(int), cmpfunc);
	for( k = 0; k < n; k++){
		l = 0; r = n-1;
		while( l < r )
		{
			if( arr[l] + arr[r] == arr[k]){
				printf("True\n");
				return 0;}
			else if( arr[l] + arr[r] < arr[k])
				l++;
			else
				r--;
		}
	}
	printf("False\n");
	return 0;
}