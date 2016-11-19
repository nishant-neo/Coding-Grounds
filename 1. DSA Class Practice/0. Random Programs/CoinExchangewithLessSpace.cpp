#include <iostream>
#include <limits.h>
#define MIN(a,b) a<b?a:b

using namespace std;

int nCoinsF( int coins[], int n, int W){
    int V[W+1];
    V[0] = 0;
    for( int i = 1 ; i <= W; i++)
        V[i] = INT_MAX-2*W;
    for( int i = 1; i <= n; i++)
    {
        for( int j = coins[i]; j <= W; j++)
        {
            V[j] = MIN((V[j - coins[i]] + 1),V[j]);
        }
    }
//    for( int i = 1 ; i <= W; i++)
//        cout<<V[i]<< " ";

    return V[W];
}
int main()
{
    int coins[] = { 0, 2, 7 ,10};
    int W = 14;
    int nCoins = nCoinsF(coins, 3,  W);
    cout<<nCoins<<endl;
    return 0;
}

