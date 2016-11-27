#include <iostream>
using namespace std;
int max(int a, int b, int c)
{
	int t = a > b ? a:b;
	return t > c?t:c;
}

int main()
{
    int n;
    cin>>n;
    int A[n+2][n+2];
    int R[n+2][n+2];
    for( int i = 1; i <= n; i++)
    	for( int j = 1; j <= n; j++)
			cin>>A[i][j];
	for( int i = 0; i <= n; i++)
		R[n][i] = A[n][i];
	for( int i = 0; i <= n; i++){
		R[0][i] = 0; R[i][0] = 0; R[i][n+1] = 0;R[n+1][i] = 0;}
	for( int j = n-1; j > 0; j--)
	{
		for( int i = 1; i <= n; i++)
		{
			R[j][i] = A[j][i] + max( R[j+1][i-1], R[j+1][i+1], R[j+1][i]);
		}
	}
	int maxV = 0;
	for( int i = 0; i <= n; i++){
		maxV = max( maxV, R[1][i], -1);
	}
	cout<<maxV<<endl;
    return 0;
}
