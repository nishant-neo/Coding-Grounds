#include <iostream>

using namespace std;

void printArray( int T[][15], int n, int W)
{
    for( int i = 1; i <= W; i++){
        for( int j = 1; j <= n; j++)
        {
            cout<<T[i][j] << " ";
        }
        cout<<endl;
    }
}
int nWaysF( int coins[], int n, int W){
    int T[W+1][n+1];
    for( int i = 0; i <= W; i++)
        T[i][0] = 0;//setting infinite
    for( int j = 0; j <= n; j++)
        T[0][j] = 1;
    for( int j = 1; j <= n; j++){
        for( int i = 1; i <= W; i++)
        {
            T[i][j] = T[i][j-1];
            if( coins[j] <= i)
                T[i][j] =  T[i][j]+ T[i-coins[j]][j];
        }
    }
    return T[W][n];
}
int main()
{
    int coins[] = { 0, 1, 7 ,10};
    int W = 15;
    int nWays = nWaysF(coins, 3,  W);
    cout<<nWays<<endl;
    return 0;
}
