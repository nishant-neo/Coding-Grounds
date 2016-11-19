#include <stdio.h>
#include <iostream>

using namespace std;

int min(int a, int b)
{
    return a< b? a:b;
}
int check( int A[], int k){
    int i;
    //cout<<"HHH"<<endl;
    for( i = 1; i <= k; i ++){
        if( A[i] == 0)
            return 0;
    }
    return 1;
}

int main()
{
    int i, j, jMin, iMax, maxSpan;
    int arr[] = { 1,1,1,1,2,2,2,1,3,3,2,4,4,4,3,2,2,1,1,1};
    int len = 19;
    int k = 4;//th value of k
    int count[k+1];
    for( i = 0; i <= k; i++)
        count[i] = 0;

    i = 0, j = 0, jMin = len-1, iMax = -1, maxSpan =0;
    while( j < len ){
        count[arr[j]]++;
        if( check(count, k) == 1)
        {
            if( (j-i) > maxSpan){
                maxSpan = j-i;
                iMax = i;
                jMin = j;}
            while( i < j)
            {
                count[arr[i]]--;
                if( check(count, k) == 1)
                    i++;
                else{
                    count[arr[j]]++; break;
                }

            }
            iMax = max( iMax, i);
            maxSpan = j-i;

        }
        j++;
    }
    cout<< iMax <<" "<<jMin<<endl;


}
