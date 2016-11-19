#include <iostream>
#include <vector>
#define ll long long int
using namespace std;

int main()
{
	int t,n,x,i;
	cin>>t;
	while(t--){
		cin>>n>>x;
		int arr[n];
		for( i = 0; i < n; i++ )
			cin>> arr[i];
		long long int sum = 0, j = 0, flag = 1;
		for( i = 0; i < n; i++)
		{
			sum += arr[i];
			if( sum == x){
				flag = 0;
				cout<<"YES\n";
				break;
			}
			while( sum > x){
				sum -= arr[j];
				j++;
				if( sum == x){
					flag = 0;
					cout<<"YES\n";
					break;
				}
			}
		}
		if( flag )
			cout<<"NO\n";
	}

    return 0;
}
