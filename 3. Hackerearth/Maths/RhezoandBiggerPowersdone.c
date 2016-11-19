#include <stdio.h>

#define ll long long
const int  M = 1e9 + 7;

ll  largenumber(char* srr){
	ll lnum = 0;
	int i, len = 0;
	while( srr[len] != '\0')
        len++;
	for (i = 0; i< len; i++){

		lnum = ((lnum * 10) % (M - 1) + (srr[i] - '0')) % (M - 1);
	}
	return lnum;
}
ll mypow(ll a, ll b) {
	if (b == 0) return 1;
	if (b % 2 == 0)
	{
		ll c = mypow(a, b / 2);
		return (c * c) % M;
	}
	return (a * mypow(a, b - 1)) % M;
}
int main()
{
    char str[100010];
	ll int a, b;
	scanf("%d %s",&a,&str);
	b = largenumber(str);
	b = b%M;
	printf("%u", mypow(a, b) );
	return 0;
}
