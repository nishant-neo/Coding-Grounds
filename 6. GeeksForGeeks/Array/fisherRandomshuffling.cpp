#include <iostream>
#include <stdlib.h>
#include <time.h>
 using namespace std;
// A utility function to swap to integers
void swap (int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
void printArray (int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout<< arr[i]<<" ";
    cout<<endl;
}
void randomize ( int arr[], int n )
{
    srand ( time(NULL) );
    for (int i = n-1; i > 0; i--)
    {
        int j = rand() % (i+1);
        swap(&arr[i], &arr[j]);
    }
}

// Driver program to test above function.
int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int n = sizeof(arr)/ sizeof(arr[0]);
    printArray(arr, n);
    randomize (arr, n);
    printArray(arr, n);
    return 0;
}
