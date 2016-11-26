#include <iostream>
#define ll long long int

using namespace std;

bool isSubsetSum(int set[], int n, int sum)
{
    bool subset[sum+1][n+1];
    for (int i = 0; i <= n; i++)
        subset[0][i] = true;
    for (int i = 1; i <= sum; i++)
        subset[i][0] = false;
    for (int i = 1; i <= sum; i++){
       for (int j = 1; j <= n; j++){
            subset[i][j] = subset[i][j-1];
            if (i >= set[j-1])
                subset[i][j] = subset[i][j] || subset[i - set[j-1]][j-1];
       }
    }
    return subset[sum][n];
}
int main()
{
    int t, n;ll sum;
    cin>>t;
    while( t-- )
    {
        sum = 0;
        cin>>n;
        int A[n];
        for( int i = 0; i < n; i++){
            cin>>A[i];
            sum = sum + A[i];
        }
        if( sum % 2 != 0)
            cout<<"NO"<<endl;
        else{
            if(isSubsetSum( A, n, sum/2))
                cout<<"YES"<<endl;
            else
                cout<<"NO"<<endl;
        }
    }
	return 0;
}
