#include <stdio.h>
#define M 100

int bin[100000];
int biszero(int* b, int len)
{
	int i = len-1;
	while( i >= 0 )
	{
		if( b[i] != 0)
			return 0;
		i--;
	}
	return 1;
}
void dividebytwo(int* b, int len)
{
	int i = 0, x = 0;
	while( b[i] == 0)
			i++;
	while( i < len ){
		x = x * 10 + b[i];
		if( x == 1){
			b[i] = 0;
			x = x*10 + b[++i];
		}
		b[i] = x / 2;
		x = x % 2;
		i++;
	}
}
int decTobin( int n[], int len)
{
    int i = 0, k = 0;
    while( biszero(n, len) != 1)
    {
        if( n[len-1] % 2 == 0)
            bin[i] = 0;
        else
            bin[i] = 1;
        dividebytwo( n, len);
        i++;
    }
    for( k = 0; k < i / 2; k++){
        int t = bin[i-k-1];
        bin[i-k-1] = bin[k];
        bin[k] = t;
    }
    return i;
}
void printMatrix( int A[][2] )
{
    int i, j;
    for( i = 0; i < 2; i++){
        for( j = 0; j < 2; j++)
        {
            printf("%d ",A[i][j]);
        }
        printf("\n\n");
    }
}
void printArray( int *n, int len)
{
    int i =0;
    for( i = 0; i < len; i++)
        printf("%d ",n[i]);
    printf("\n");
}
void dividebytwobin( int* len )
{
    (*len)--;
}
void matrixMulti( int A[][2], int B[][2])
{
   /* printf("the matrix A is:\n ");
    printMatrix(A);
    printf("the matrix B is:\n ");
    printMatrix(B);*/
    int C[2][2];
	C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0];
	C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1];
	C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0];
	C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1];
	A[0][0] = (C[0][0])%M;
	A[0][1] = (C[0][1])%M;
	A[1][0] = (C[1][0])%M;
	A[1][1] = (C[1][1])%M;
}
int power( int n[], int len)
{

    int A[2][2] = {{1,1},{1,0}};
	int Y[2][2] = {{1,0},{0,1}};
	while(len != 0 || biszero(n,len) != 1)
	{
		if( n[len-1] == 1)
			matrixMulti( Y, A);
		matrixMulti( A, A);

		dividebytwobin( &len);//to be replaced by DIVIDEBYTWO()
	}
	return Y[1][0];
}

int main()
{
    int arr[] = {1,2,3,4,5,6};
    int len = decTobin(arr, 6);
    printArray(bin,len);
    printf("%d",power(bin,len));
	return 0;
}
