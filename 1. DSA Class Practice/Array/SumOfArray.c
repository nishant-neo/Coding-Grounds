#include <stdio.h>

int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}
void find(int arr[], int n, int x)
{
	int l, r;
	l = 0;
	r = n-1;
	qsort(arr, n, sizeof(int), cmpfunc);
	while( l < r ){
		//printf("%d %d\n", arr[l], arr[r]);
		if( arr[l] + arr[r] == x){
			printf("%d %d\n",arr[l],arr[r]);
			return;
		}
		else if( arr[l] + arr[r] < x)
			l++;
		else
			r--;
	}
	printf("No match\n");
}

int main()
{
	int arr[] = { 2,6,3,5,32,3,1,9};
	find( arr, 8, 42);
	return 0;
}