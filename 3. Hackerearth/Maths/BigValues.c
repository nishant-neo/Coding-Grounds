#include <stdio.h>
#define M 1000000007
#define LLU long long unsigned int

int main()
{
	LLU n, i, x =301388891;
	scanf("%llu",&n);
		x = (x * (n)) % M;
		x = (x * (n-1)) % M;
		x = (x * (n-2))% M;
		x = (x * (n-3)) % M;
		x = (x * (n-4)) % M;
		x = (x * (n-5)) % M;
	printf("%llu\n",x);
}

