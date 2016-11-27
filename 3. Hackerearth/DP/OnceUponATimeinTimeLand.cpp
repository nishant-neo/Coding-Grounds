#include <stdio.h>
#include <limits.h>
#define ll long long
#define MAX(a,b) a > b ? a : b;

int main()
{
    ll t, n, k, i , j;
    scanf("%lli",&t);
    while( t-- ){
    	scanf("%lli %lli",&n,&k);
    	ll A[n+2], R[n+2];
    	A[0] = 0;
    	ll maxV = INT_MIN;
    	for(  i = 1; i <= n; i++){
    		scanf("%lli", &A[i]);
    		R[i] = A[i];
    		maxV = MAX(maxV, R[i]);
    	}

    	for(  i = k+2; i <= n; i++)
    	{
//    		R[i] = A[i];
    		for(  j = i-k-1; j > 0; j--)
    		{
    			R[i] = MAX( R[i], (R[j] + A[i]));
    		}
    		maxV = MAX(maxV, R[i]);
    	}
    	maxV = (maxV < 0)?0:maxV;
    	printf("%llu\n",maxV);
    }
    return 0;
}
