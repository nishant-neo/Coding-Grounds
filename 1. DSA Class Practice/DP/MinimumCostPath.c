#include <stdio.h>
#include <limits.h>
#define MIN( a, b) a<b?a:b
#define R 3
#define C 3

int minimum(int x, int y, int z)
{
   if (x < y)
      return (x < z)? x : z;
   else
      return (y < z)? y : z;
}
int minCostDP( int cost[R][C], int m, int n )
{
    int i, j;
    int minCostarr[R][C];
    minCostarr[0][0] = 1;
    for( i = 1; i <= m; i++)
        minCostarr[i][0] = minCostarr[i-1][0] + cost[i][0];
    for( i = 1; i <= n; i++)
        minCostarr[0][i] = minCostarr[0][i-1] + cost[0][i];
    for( i = 1; i <= m; i++){
        for( j = 1; j <= n; j++){
            minCostarr[i][j] = cost[i][j] + minimum( minCostarr[i-1][j-1], minCostarr[i][j-1], minCostarr[i-1][j] );
        }
    }
    return minCostarr[m][n];

}
int minCost( int cost[R][C], int m, int n )
{
    if( m < 0 || n < 0)
        return INT_MAX;
    else if( m == 0 && n == 0)
        return cost[m][n];
    else
        return cost[m][n] + minimum( minCost( cost, m-1, n-1), minCost( cost, m-1, n), minCost( cost, m, n-1));

}
int main()
{
    int cost[R][C] = { {1, 2, 3},
                      {4, 8, 2},
                      {1, 5, 3} };
    printf("Minimum Cost Path is: %d \n", minCost(cost, 2, 2));
    printf("Minimum Cost Path by DP is: %d ", minCostDP(cost, 2, 2));
    return 0;
}
