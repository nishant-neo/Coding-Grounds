#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int t, n;
    cin>>t;
    while( t--){
        cin>>n;
        vector <int> A(n);
        for(int i = 0; i < n; i++)
            cin>>A[i];
        sort(A.begin(), A.end());
        int count = 0;
        for( int i = n-1; i >= 1; i--){
            int l = 0, r = i-1;
            while( l < r){
                if( A[l] + A[r] > A[i]){
                    count += r - l ;
                    r--;
                }
                else
                    l++;
            }
        }
        cout<<count<<endl;
    }
	return 0;
}
