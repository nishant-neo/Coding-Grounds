#include <iostream>
#define CH cout<<"FGFG"<<endl
using namespace std;
int weights[1000009];

void merge( int* arr, int l, int r, int k)
{
    int B[r-l+2];
    int i = l, j = k+1, t = 0;
    while( i <= k && j <= r)
    {
        if( arr[i] >= arr[j]){
            weights[arr[i]] += r-j+1;
            B[t++] = arr[i++];

        }
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
    int t,i;
    cin>>t;
    while( t--){
    	int n;
    	cin>>n;
    	int arr[n+2];
    	int arr2[n+2];
    	for( i = 0; i < n; i++){
    		cin>>arr[i];
    		arr2[i] = arr[i];
    		weights[arr[i]] = 0;
    	}
    	mergeSort(arr, 0, n-1);
    	for( i = 0; i < n; i++){
            cout<<arr2[i]<<" ";
    		cout<<weights[arr2[i]]<<"\n";}
    	cout<<endl;
    }
    return 0;
}
