#include <stdio.h>
#define LLU long long unsigned int
#define MOD 1000000007

int main()
{
    LLU t, n;
    scanf("%d",&t);
    while( t-- )
    {
        scanf("%llu",&n);
        LLU temp =  ((n-1) / 2);
        LLU minx =  (((temp% MOD * temp% MOD)% MOD) * (n% MOD))% MOD;
        LLU maxx = temp;
        LLU t1 = n;
        LLU t2 = 2 * n - 1;
        if( maxx % 3 == 0)
        	maxx = maxx / 3;
        else if( t1 % 3 == 0)
        	t1 = t1 / 3;
        else
        	t2 = t2 / 3;
        maxx =(maxx * t1)%MOD;
		maxx =(maxx * t2)%MOD;
        printf("%llu %llu\n", minx , maxx);

    }
    return 0;
}
