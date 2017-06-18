#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



vector<vector<int> > threeSum(vector<int> &A) {
    cout<<"fff\n";
    int n = A.size();
    sort( A.begin(), A.end());
    vector <vector<int> > res;
    cout<<"fff\n";
    for( int i = 0; i < n; i++)
    {
        cout<<"fff\n";
        int l = i+1, r = n-1;
        cout<<i<<" "<<l<<" "<<r<<endl;
        while( l < r ){
            if( A[i] + A[l] + A[r] == 0){
                vector <int> trip;
                trip.push_back(A[i]);
                trip.push_back(A[l]);
                trip.push_back(A[r]);
                res.push_back(trip);
                l++;r--;

            }
            else if( A[i] + A[l] + A[r] < 0 )
                l++;
            else
                r--;
        }
    }
    return res;
}
int main(){
    static const int arr[] = {-1, 0, 1, 2, -1, -4};
    vector <int> A (arr, arr + sizeof(arr) / sizeof(arr[0]) );
    vector <vector<int> > res = threeSum(A);
    for( int i = 0; i < res.size(); i++)
    {
        for( int j = 0; j < res[i].size(); j++){
            cout<<res[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}
