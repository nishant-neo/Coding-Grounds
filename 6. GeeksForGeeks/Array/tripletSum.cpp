#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int t, n, B;
    cin>>t;
    while( t--){
        cin>>n>>B;
        vector<int>A(n);
        for( int i = 0; i < n; i++)
            cin>>A[i];
        sort( A.begin(), A.end());
        int flag = 1;
        for( int i = 0; i < n && flag == 1; i++){
            int l = i+1, r = n-1;
            while( l < r){
                if( A[l] + A[r] + A[i] == B){
                    flag = 0;
                    cout<<"1"<<endl;
                    break;
                }
                else if( A[l] + A[r] + A[i] > B)
                    r--;
                else
                    l++;
            }
        }
        if( flag )
            cout<<"0"<<endl;


    }
	return 0;
}
