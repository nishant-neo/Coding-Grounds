#include <stdio.h>
#define MIN(a,b) a < b? a:b
int minimum( int x, int y)
{
    return x < y ? x:y;
}
int bc( int n, int  k)
{
    if (k==0 || k==n)
        return 1;
    return bc( n-1, k) + bc(n-1, k-1);
}
int bcDP( int n, int k)
{
    int i, j;
    int arr[n+1][k+1];

    for( i = 0; i < n+1; i++){
        for( j = 0; j <= minimum(i, k); j++){
            if (j == 0 || j == i)
                arr[i][j] = 1;
            else
                arr[i][j] = arr[i-1][j] + arr[i-i][j-1];
        }
    }
    return arr[n][k];
}
int main()
{
    int n = 5, k = 2;
    //printf("Value of C(%d, %d) is %d \n", n, k, bc(n, k));
    printf("Value of C(%d, %d) is %d ", n, k, bcDP(n, k));
    return 0;
}
