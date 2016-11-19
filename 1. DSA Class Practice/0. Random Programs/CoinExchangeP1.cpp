#include <iostream>
#include <vector>
#include <limits.h>
#define MIN(a,b) a<b?a:b

using namespace std;
void printArray( int V[][15], int n, int W)
{
    for( int i = 1; i <= W; i++){
        for( int j = 1; j <= n; j++)
        {
            cout<<V[i][j] << " ";
        }
        cout<<endl;
    }
}
int nCoinsF( int coins[], int n, int W){
    int V[W+1][n+1];
    for( int i = 0; i <= W; i++)
        V[i][0] = INT_MAX;//setting infinite
    for( int j = 0; j <= n; j++)
        V[0][j] = 0;
    for( int i = 1; i <= W; i++){
        for( int j = 1; j <= n; j++)
        {
            V[i][j] = V[i][j-1];
            if( coins[j] <= i)
                V[i][j] = MIN( V[i][j], (V[i-coins[j]][j] + 1));
        }
    }
    return V[W][n];
}
int main()
{
    int coins[] = { 0, 1, 7 ,10};
    int W = 15;
    int nCoins = nCoinsF(coins, 3,  W);
    cout<<nCoins<<endl;
    return 0;
}
