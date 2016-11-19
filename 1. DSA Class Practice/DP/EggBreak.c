#include <stdio.h>
#include <limits.h>
#define MAX(a,b) a>b?a:b

int maxi(int a, int b) { return (a > b)? a: b; }
int eggDropDP( int n, int k)
{
    int i,j, l;
    int arr[n+1][k+1];
    for (i = 1; i <= n; i++)
    {
        arr[i][1] = 1;
        arr[i][0] = 0;
    }
    for (j = 1; j <= k; j++)
        arr[1][j] = j;
    for( i = 2; i <= n; i++){
        for( j = 2; j <= k; j++)
        {
                arr[i][j] = INT_MAX;int res;
                for( l = 1; l <= j; l++)
                {
                    res = 1 + maxi( arr[i-1][l-1], arr[i][j-l]);
                    if( res < arr[i][j])
                        arr[i][j] = res;
                }

        }
    }
    return arr[n][k];
}
int eggDrop( int n, int k)
{
    if( k == 1 || k == 0 )
        return k;
    if( n == 1)
        return k;
    int min = INT_MAX, i, x;
    for(i = 1; i <= k; i++){
        x = MAX( eggDrop( n-1 , i-1 ), eggDrop( n , k-i ) );
        if( x < min)
            min = x;
    }
    return min + 1;
}
int main()
{
    int n = 2, k = 100;
   // printf ("\nMinimum number of trials in worst case with %d eggs and "
   //          "%d floors is %d \n", n, k, eggDrop(n, k));
    printf ("\nMinimum number of trials in worst case with %d eggs and "
             "%d floors is %d \n", n, k, eggDropDP(n, k));
    return 0;
}
