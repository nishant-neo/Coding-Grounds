#include <stdio.h>
#include <stdlib.h>

int swap( int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
int median( int* A, int l, int r)//0 indexed
{
    int i, j;
    for( i = l; i <= l+2; i++){
        int temp = i;
        for( j = i+1; j <= r; j++)
        {
            if( A[temp] > A[j])
                temp = j;
        }
        swap( &A[i], &A[temp]);
    }
    return A[(l+r)/2];
}
int goodPivot(int A[], int l, int r)//1 indexed
{
    //printf("goodpivot%d %d\n",l,r);
    if( (r-l) < 5)
        return median( A, l-1, r-1);
    int i, j = l-1;
    for( i = l-1; i < r; i = i + 5)
        j = median( A, i, (i+4 < r ? i+4 : r-1));
    j = l-1;
    for( i = l + 1; i < r; i = i + 5)
        swap( &A[i], &A[j++]);

    return goodPivot( A, l, l+(r-l)/5+1);
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
	return r+1;
}
int findRank( int* A, int i, int j, int r)//1 indexed
{
	//printf("findrank %d %d %d\n",i,j,r);
	int p, k;
	p = goodPivot( A, i, j);
	k = partition( A, i ,j, p);
	if( r == j - k + 1)
    {
        //printf("result%d\n",p);
		return p;
    }
	else if( r < (j - k + 1))
		findRank( A, k+1, j, r);
	else
        findRank( A, i, k, r-j+k );
}
int main()
{
	int A[] = { 1, 6, 5, 81, 2, 7, 29, 34, 100, 67, 55, 35, 88, 87, 43, 56, 76, 54, 90, 11, 34, 456, 67, 78, 89, 48, 77, 80};
	printf("%d\n",findRank( A, 1, 28, 28));
	printArray(A, 1,28);
	return 0;
}
