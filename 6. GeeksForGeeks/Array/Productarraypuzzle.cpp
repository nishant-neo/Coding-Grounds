#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t, n;
    cin>>t;
    while( t--){
        cin>>n;
        vector <int> C(n);
        for( int i = 0 ; i < n; i++)
            cin>>C[i];
        vector <long long int> prod(n,1);
        vector <long long int> prod2(n,1);
        for( int i = 1; i < n; i++)
            prod[i] = prod[i-1] * C[i-1];
        for( int i = n-2; i >= 0; i--)
            prod2[i] = prod2[i+1] * C[i+1];
        for( int i = 0; i < n ; i++)
            cout<<prod[i]*prod2[i]<<" ";
        cout<<endl;

    }
	return 0;
}
