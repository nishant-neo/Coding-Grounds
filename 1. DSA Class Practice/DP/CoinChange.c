#include <stdio.h>
#include <limits.h>
#define MIN(a,b) a < b? a:b
int countIt( int* arr, int m, int S)
{
    int i, j;
    int change[S+1];

    for( i = 0; i < S+1; i++)
        change[i] = 10000;
    change[0] = 0;
    for( i = 0; i < m; i++)
        change[arr[i]] = 1;
    for( i = arr[0]+1; i < S+1; i++)
    {
        //printf("##%d %d\n", i, change[i]);
        for( j = 0; j < m; j++)
        {
            if( i < arr[j] || change[i] == 1 )
                break;
            else{
                change[i] = MIN( (change[i]), change[i-arr[j]] + 1);
            }
            //printf("@@%d %d\n", arr[j], change[i]);
        }
        //printf("##%d %d\n", i, change[i]);
    }
    return change[S];


}
int main()
{
    int i, j;
    int arr[] = {2, 3, 5, 6};
    int m = sizeof(arr)/sizeof(arr[0]);
    printf("Minimum coin change: %d ", countIt(arr, m, 10));
    getchar();
    return 0;
}
