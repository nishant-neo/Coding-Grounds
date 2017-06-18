
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int t, n, B;
    cin>>t;
    while( t-- ){
        cin>>n;
        cin>>B;
        vector <int> A(n);
        vector<int> sum(n,0);
        for(int i = 0; i < n; i++){
            cin>>A[i];
            if( i == 0)
                sum[i] = 0;
            else
                sum[i] = sum[i-1] + A[i-1];
        }
        int l = 0, r = 0, flag = 1;
        while( r < n ){
            //cout<<sum[l]<<" "<<sum[r]<<endl;
            if( r== l)
                r++;
            if( A[r] + sum[r] - sum[l] == B){
                flag = 0;
                cout<<l+1<<" "<<r+1<<endl;
                break;
            }
            else if( A[r] + sum[r] - sum[l] > B)
                l++;
            else
                r++;
        }
        if( flag)
            cout<<"-1"<<endl;

    }
	return 0;
}
