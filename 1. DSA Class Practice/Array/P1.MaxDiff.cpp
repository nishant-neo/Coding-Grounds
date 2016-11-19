#include <iostream>
#include <limits.h>
using namespace std;

int main()
{
    int A[] ={ 2,1,356,5,43,55,4,2,5,77,3,112};
    int len = 12;
    int i = 0;
    int max = INT_MIN;
    for( int j = 0; j < len; j++)
    {
        if( (A[j] - A[i]) > max)
            max = A[j] -A[i];
        if( A[j] < A[i])
            i = j;
    }
    cout<<max<<"\n";
    return 0;

}
