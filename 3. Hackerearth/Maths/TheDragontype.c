#include <stdio.h>
#define LL long long
LL max( LL a, LL b)
{
	return a > b? a:b;
}
LL power( LL a, LL b, LL MOD)
{
	LL res=1;
    LL x=a;
    while(b)
    {
        if(b&1)
            res=(res*x)%MOD;
        x=(x*x)%MOD;
        b>>=1;
    }
    return res%MOD;
}
LL invmod( LL i, LL p)
{
	return power( i, p-2, p );
}
int main()
{
	LL n, p, i;
	scanf("%llu %llu", &n, &p);
	LL A[n];
	LL countit[p+1];
	int done[p+1];

	for( i = 0; i <= p; i++){
		countit[i] = 0;
		done[i] = 0;
	}
	for( i = 0; i < n; i++){
		scanf("%llu",&A[i]);
		A[i] = A[i] % p;
		countit[A[i]]++;
	}
	LL ans = 0;
	for( i = 0; i < p; i++)
	{
	    if( done[i])
            continue;
		LL x=invmod(i,p);
		if(i!=x)
            ans+=max(countit[i],countit[x]);
        done[i]= 1;
        done[x]= 0;
	}
	//printf("RTR");
	printf("%llu\n",ans  + countit[0]);

}
