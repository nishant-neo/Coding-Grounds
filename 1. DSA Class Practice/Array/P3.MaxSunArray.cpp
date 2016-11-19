#include <iostream>

using namespace std;
int main()
{
    int A[] ={ 2,1,-356,5,43,-155,4,2,5,77,3,-112};
    int len = 12;
    int sum = 0;
    int max = A[0];
    int i = 0;
    for( int j = 0; j < len; j++){
        sum = sum + A[j];
        if( sum > max)
            max = sum;
        if( sum < 0)
        {
            sum = 0;
            i = j + 1;
        }
    }
    cout<<max;
    return 0;

}

