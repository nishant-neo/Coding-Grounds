#include <iostream>

using namespace std;

string convert(string A, int B) {
    cout<<"fd";
    int n = A.size();
    if( n <= 1)
        return A;
    string res = "";
    for( int i = B; i > 0; i--){
        {
            cout<<"GRGFR"<<endl;
            for( int j = B-i; j < n; j = j + (2*(i -1)) )
            {
                cout<<"A"<<endl;
                res += A[j];
            }
        }
    }
    return res;
}
int main()
{
    string A = "ABCD";
    cout<<convert(A,2);
    return 0;
}
