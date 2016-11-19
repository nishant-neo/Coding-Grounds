#include <iostream>
//#include <vector>
#include <math.h>
using namespace std;
int isPrime[5001];

void prime( )
{
	int i;
	isPrime[2] = 1;
	for( i = 3; i <= 5000; i = i + 2)
		isPrime[i] = 1;
	for( i = 3; i*i <= 5000 ; i++){
        if( isPrime[i] == 1){
            for (int j=i*2; j<=5000; j += i)
                isPrime[j] = 0;
        }
	}
}
int main()
{
	int n,x,j, i;
	cin>>n;
	int A[n];
	for( i = 0; i < n; i++)
		cin>> A[i];
    prime();
	for( i = 0; i <= 5000; i++){
		if( isPrime[i] ==1 )
			cout<<i<<" ";
	}
    return 0;

}

