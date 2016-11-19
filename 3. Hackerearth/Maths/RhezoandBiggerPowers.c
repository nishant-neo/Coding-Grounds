#include <stdio.h>
#define MOD 1000000007
#include <limits.h>

int biszero(int* b, int len)
{
	int i = len-1;
	while( i >= 0 )
	{
		if( b[i] != 0)
			return 0;
		i--;
	}
	return 1;
}
void dividebytwo(int* b, int len)
{
	int i = 0, x = 0;
	while( b[i] == 0)
			i++;
	while( i < len ){
		x = x * 10 + b[i];
		if( x == 1){
			b[i] = 0;
			x = x*10 + b[++i];
		}
		b[i] = x / 2;
		x = x % 2;
		i++;
	}
}
 int power( long long int a, int* b, int len)
{
	if( biszero(b, len) )
		return 1;
    if( b[len-1] % 2 == 0)
    {
        dividebytwo(b,len);
        long long unsigned int x = power(a,b,len) % MOD;
        return (x*x)% MOD;
    }
    else
    {
        dividebytwo(b,len);
        long long unsigned int x = power(a,b,len) % MOD;
        return ((a%MOD)*((x*x)% MOD))%MOD;
    }
}
int main()
{

	int i = 0;
	char b[100010];
	int bint[100010];
    long long unsigned int a;
    scanf("%llu %s", &a, &b);
    while( b[i] != '\0')
    {
    	bint[i] = b[i]-'0';
    	i++;
    }
    printf("%d\n",power( a, bint, i));
    return 0;
}

