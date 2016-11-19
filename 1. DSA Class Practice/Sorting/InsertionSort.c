#include <stdio.h>

void printArray( int *arr, int n)
{
    int i;
    for( i = 0; i < n; i++)
        printf("%d ",arr[i]);
}

void insertionSort( int* arr, int n)
{
    int i, pivot, j;
    for( i = 1; i < n; i++){
        pivot = arr[i];
        j = i-1 ;
        while( arr[j] > pivot && j >= 0){
            arr[ j+1 ]  = arr[j];
            j--;
        }
        arr[j+1] = pivot;

    }

}
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    printf("Unsorted array: \n");
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n);
    insertionSort(arr, n);
    printf("\nSorted array: \n");
    printArray(arr, n);
    return 0;
}

