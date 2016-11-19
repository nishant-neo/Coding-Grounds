#include <stdio.h>
#include <limits.h>
#define LLU long long int

int main()
{
	LLU n, k, i;
	scanf("%llu %llu",&n, &k);
	int A[n+1];
	int B[n+3];
	LLU max = LLONG_MIN, sum1 = 0, sum2 = 0, t;
	while( k-- ){
		sum1 = 0, sum2 = 0;
		for( i = 1; i <= n; i++)
			scanf("%d",&A[i]);
		for( i = n/2 + 1; i <= n; i++)
			sum1 = sum1 + A[i];
		for( i = 1; i <= (n/2); i++)
			sum2 = sum2 + A[i];
		LLU temp = 	sum1 > sum2 ? sum1: sum2;
		max = max > temp ? max: temp;
		for( i = 1; i <= n/2; i++)
		{
			sum2 = sum2 - A[(n/2) - i + 1] + A[ n - i + 1];

			if( max < sum2)
				max = sum2;
		}

	}
	printf("%llu\n",max);



}
