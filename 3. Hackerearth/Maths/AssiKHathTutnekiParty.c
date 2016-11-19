
#include <stdio.h>
#define LLU long long unsigned int
#define MOD 1000000007

int power(LLU a, LLU b)
{
	if( b == 0)
		return 1;
	if (b % 2 == 0)
	{
		LLU c = power(a, b / 2);
		return (c * c) % MOD;
	}
	return (a * power(a, b - 1)) % MOD;
}
int main()
{
    LLU t,b,a, k;
    scanf("%llu",&t);
    while( t -- )
    {
    	scanf("%llu %llu %llu", &a,&b,&k);
    	printf("%llu %llu\n",(a+b),k);
    	printf("%d\n",power((a+b), k));
    }
    return 0;
}
