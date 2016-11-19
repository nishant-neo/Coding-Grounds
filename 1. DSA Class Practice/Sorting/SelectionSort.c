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
void selectionSort( int* arr, int n)
{
    int i, j, temp_pos;
    for( i = 0; i < n; i++){
        temp_pos = i;
        for( j = i + 1; j < n; j++)
        {
            if( arr[j] < arr[temp_pos])
                temp_pos = j;
        }
        swap( &arr[i], &arr[temp_pos]);
    }

}
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    printf("Unsorted array: \n");
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n);
    selectionSort(arr, n);
    printf("\nSorted array: \n");
    printArray(arr, n);
    return 0;
}

