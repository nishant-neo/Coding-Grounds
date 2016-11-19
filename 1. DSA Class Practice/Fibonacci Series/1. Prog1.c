#include <stdio.h>
#define M 100
#define LLU long long unsigned int
#define LEN 10000

int C[2][2];
int A[LEN];
int randomNumb()
{
    return rand()%9 + 1;
}
void printArray( int *n, int len)
{
    int i =0;
    for( i = 0; i < len; i++)
        printf("%d ",n[i]);
    printf("\n");
}
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
	//printArray(b,len);
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
	while( biszero(n,len) != 1)
	{
		if( n[len-1] % 2 != 0)
			matrixMulti( Y, A);
		matrixMulti( A, A);
		dividebytwo(n, len);//to be replaced by DIVIDEBYTWO()

	}
	return Y[1][0];
}

int main()
{
    int len = LEN,i;
    for( i = 0; i < len ;i++)
        A[i] = randomNumb();
    printf("%d",power(A,len));
	return 0;
}
