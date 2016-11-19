#include <stdio.h>


void quickSort( int* arr, int l, int r){
    int p = r-1;
    int k  = partitions( arr, l , r, p);
    quickSort( arr, l, k);
    quickSort( arr, k+1, r);
}
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    printf("Unsorted array: \n");
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n);
    printf("\n");
    quickSort(arr, 0, n-1);
    printf("\nSorted array: \n");
    printArray(arr, n);
    return 0;
}
