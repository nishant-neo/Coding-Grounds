#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n, t;
    cin>>t;
    vector<int>A(50010,0);
        A[1] = 1;
        for( int i = 1; i <= 10000; i++ ){
            if( A[i] == 1){
                A[2*i] = 1;
                A[3*i] = 1;
                A[5*i] = 1;
            }
        }
    while(t--){
        cin>>n;
        int count = 0, i;
        for( i = 1; i <= 50000; i++){
            if( A[i] == 1)
                count++;
            if( count == n)
                break;
        }
        cout<<i<<endl;
    }
	return 0;
}
