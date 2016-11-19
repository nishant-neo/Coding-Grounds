#include <stdio.h>

void printArray( int *arr, int n)
{
    int i;
    for( i = 0; i < n; i++)
        printf("%d ",arr[i]);
}
void merge( int* arr, int l, int r, int k)
{
    int B[r-l+2];
    int i = l, j = k+1, t = 0;
    while( i <= k && j <= r)
    {
        if( arr[i] <= arr[j])
            B[t++] = arr[i++];
        else
            B[t++] = arr[j++];
    }
    while( i <= k)
        B[t++] = arr[i++];
    while( j <= r)
        B[t++] = arr[j++];
    t = 0;
    while( l <= r)
        arr[l++] = B[t++];
}
void mergeSort( int* arr, int l, int r)
{
    if( l < r){
        int k = (l+r) / 2;
        mergeSort( arr, l , k);
        mergeSort( arr, k+1, r);
        merge( arr, l, r, k);
    }

}
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    printf("Unsorted array: \n");
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n);
    printf("\n");
    mergeSort(arr, 0, n-1);
    printf("\nSorted array: \n");
    printArray(arr, n);
    return 0;
}

