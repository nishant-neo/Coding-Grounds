#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

int main()
{
    int t, n;
    cin>>t;
    while( t--){
        cin>>n;
        vector <int> A(n);
        for( int i = 0; i < n; i++){
            cin>>A[i];
        }
        int minIndex = 0, maxVal = INT_MIN;
        for( int i = 1 ; i < n; i++){
            if( A[i] - A[minIndex] > maxVal)
                maxVal = A[i] - A[minIndex];
            if( A[i] < A[minIndex])
                minIndex = i;
        }
        cout<<maxVal<<endl;
    }
	return 0;
}
