#include <iostream>

using namespace std;
int main()
{
    int A[] ={ 2,1,356,5,43,55,4,2,5,77,3,112};
    int len = 12;
    int k = 4;
    int i = 0;
    int max = A[k-1] - A[0];
    for( int j = k-1; j < len; j++)
    {
        if( (A[j] - A[i]) > max)
            max = A[j] - A[i];
        if( A[j-k] < A[i])
            i = j-k;
    }
    cout<<max<<"\n";
    return 0;

}
