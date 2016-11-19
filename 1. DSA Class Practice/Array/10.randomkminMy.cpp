#include <stdio.h>
#include <stdlib.h>

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
    for( i = i-1; i <= r+1; i++)
    {
        if( A[i] == p)
            swap(&A[i],&A[r]);
    }
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
}
int main()
{
	int A[] = {  1, 6, 5, 81, 3, 7, 33, 34, 100, 67, 55, 35, 88, 89, 43, 56, 76, 54, 90, 11, 34, 456, 67, 78, 89, 48, 77, 80};
	//printf("%d",findRank( A, 1, 9, 8));
	int k = 10, in = 0, random, loc,n = 28 ;
	int B [2*k];
	for( int i = 0; i < 2*k; i++)
        B[i] = A[in++];
    while( in < n){
        int i = 2*k;
        random = pivot(B, 1, 2*k );
        loc = partition(B, 1, i, random);
        if( loc < k )
            continue;
        else if( loc == k)
        {
            for( i = k; i < 2*k&& in < n; i++)
                B[i] = A[in++];
        }
        else
        {
            for( i = loc+1; i < 2*k && in < n; i++)
                B[i] = A[in++];
        }
    }
    printf(" %d \n",findRank( B, 1, 2*k, k));
    printArray(B,1,k);

	return 0;
}
