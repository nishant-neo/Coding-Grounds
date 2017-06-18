#include <iostream>
#include <vector>
#include <limits.h>
#define MAX(a,b) a > b ? a : b
#define MIN(a,b) a < b ? a : b
using namespace std;
int main()
{
    int t, n;
    cin>>t;
    while( t--){
        cin>>n;
        vector <int> A(n);
        for( int i = 0; i < n; i++)
            cin>>A[i];
        long long int minTill = 1, maxTill = 1, maxProd = INT_MIN;
        for( int i = 0; i < n; i++){
            if( A[i] > 0){
                minTill = MIN( (A[i]*minTill), 1);
                maxTill = maxTill * A[i];
            }
            else if( A[i] == 0){
                minTill = 1;
                maxTill = 1;
            }
            else{
                int temp = maxTill;
                maxTill = MAX((minTill * A[i]),1);
                minTill = temp * A[i];
            }
            maxProd = MAX( maxProd, maxTill);
        }
        cout<<maxProd<<endl;
    }
	return 0;
}
