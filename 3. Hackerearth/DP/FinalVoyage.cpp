#include <iostream>
#include <vector>
using namespace std;
int max( int a, int b){
	return a > b ? a:b;
}

int main()
{
    int t, n, W;
    cin>>t;
    while( t-- )
    {
    	cin>>n>>W;
    	vector <pair< int, int> > items(n);
    	for( int i = 0; i < n; i++)
    		cin>>items[i].first;
    	for( int i = 0; i < n; i++)
    		cin>>items[i].second;
    	int A[n+1][W+1];
    	for( int k = 0; k <= n; k++)
			for( int i = 0; i < W+1; i++)
				A[k][i] = 0;
		for( int k = 0; k <= n; k++)
		{
			for( int i = 0; i < W+1; i++)
			{
				if (i==0 || k==0)
               		A[k][i] = 0;
				else if( (i - items[k-1].first) >= 0)
					A[k][i] = max(A[k-1][i - items[k-1].first ] + items[k-1].second, A[k-1][i]);
				else
                 	A[k][i] = A[k-1][i];
			}
		}
		cout<<A[n][W]<<endl;
    }
    return 0;
}
