#include <stdio.h>
void printArray( int *arr, int n)
{
    int i;
    for( i = 0; i < n; i++)
        printf("%d ",arr[i]);
}
void swap( int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}

void bubbleSort( int* arr, int n)
{
    int i, j;
    for( i = 0; i < n; i++){
        for( j = 0; j < n - i -1; j++)
        {
            if( arr[j+1] < arr[j])
                swap(&arr[j+1], &arr[j]);
        }
    }

}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    printf("Unsorted array: \n");
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n);
    bubbleSort(arr, n);
    printf("\nSorted array: \n");
    printArray(arr, n);
    return 0;
}
