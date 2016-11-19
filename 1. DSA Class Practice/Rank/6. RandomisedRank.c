#include <stdio.h>
#include <stdlib.h>
int count = 0;
int pivot( int* A, int i , int j)
{
    if( i == j)
        return A[i-1];
	return A[rand() % (j-i) + i];
}
void swap( int *x, int* y)
{
	int t = *x;
	*x = *y;
	*y = t;
}
void printArray( int * A, int i, int j)
{
    for( i = i-1;i<j;i++){
        printf("%d ",A[i]);
    }
    printf("\n");
}
int partition( int* A, int i, int j, int p)
{
    //printf("ggg %d %d %d\n",i,j,p);
	int  l = i-1, r = j-1;
	while( l < r){
		while( A[l] <= p )
			l++;
		while( A[r] > p)
			r--;
		if( l < r)
			swap( &A[l], &A[r]);
	}
	int x = i;
	//printf("VVFVFV\n");
    for( i = i-1; i <= r+1; i++)
    {
        if( A[i] == p)
            swap(&A[i],&A[r]);
    }
    //printArray(A, x,j);
	return r+1;
}
int findRank( int* A, int i, int j, int r)//1 indexed
{
	int p, k;
	p = pivot( A, i, j);
	k = partition( A, i ,j, p);
	if( r == j - k + 1)
		return p;
	p = pivot( A, i, j);
	k = partition( A, i ,j, p);
	if( r == j - k + 1)
		return p;
	else if( r < (j - k + 1))
		findRank( A, k+1, j, r);
	else
		findRank( A, i, k-1, r-j+k-1 );
		//printf("FFF\n");
}
int main()
{
	int A[] = {  1, 6, 5, 81, 3, 7, 33, 34, 100};// 67, 55, 35, 88, 89, 43, 56, 76, 54, 90, 11, 34, 456, 67, 78, 89, 48, 77, 80};
	printf("%d",findRank( A, 1, 9, 8));
	return 0;
}
