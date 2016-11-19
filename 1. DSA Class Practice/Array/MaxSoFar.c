#include <stdio.h>

int main()
{
	int i, j, max;
	int A[] = { 2,6,3,5,32,3,1,9};
	int n = 8;
	int B[n];
	B[0] = A[0];
	for( i =1; i < n; i++){
		if( B[i-1] < A[i])
			B[i] = A[i];
		else
			B[i] = B[i-1];
	}
	max = A[0] - A[1];
	for( i = 1; i < n; i++)
	{
		if( max < ( B[i-1] -A[i]))
			max = B[i-1] -A[i];
	}
	printf("Maximum differnece : %d\n",max);

	int l = 3;
	max = A[0] - A[l];
	for( i = l; i < n; i++)
	{
		if( max < ( B[i-l] -A[i]))
			max = B[i-l] -A[i];
	}
	printf("Maximum differnece : %d\n",max);


}