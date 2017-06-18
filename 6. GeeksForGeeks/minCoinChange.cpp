#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;
int min( int a, int b){
    return a < b ? a : b;
}
int main()
{
    int t, n, amt;
    cin>>t;
    while(t--){
        cin>>n>>amt;
        vector<int> C(n);
        for( int i = 0; i < n; i++)
            cin>>C[i];
        vector <int> CC(3*amt, INT_MAX);
        CC[0] = 0;
        for( int i = 0; i <= amt; i++){
            if( CC[i] != INT_MAX){
                for( int j = 0; j < n; j++){
                    CC[i+C[j]] = min(CC[i+C[j]], CC[i] + 1);
                }
            }
        }
        //for( int i = 0; i <= amt; i++)
        //    cout<<CC[i]<<" ";
        if( CC[amt] == INT_MAX)
            cout<<-1<<endl;
        else
            cout<<CC[amt]<<endl;
    }
	return 0;
}
