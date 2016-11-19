#include <stdio.h>
#define LLU long long unsigned int
int n[100000001];
LLU mod( int n[], LLU len, LLU m)
{
    LLU i, lr = 0;
    for( i = 0; i < len; i++){
        lr = lr*10 + n[i];
        if( lr > 0)
            lr = lr % m;
        else
            continue;
    }
    return lr;
}
void random(LLU len)
{
    LLU i;
    srand(time(NULL));
    for( i = 0; i < len; i++)
    {
        n[i] = rand() % 10;
    }
}
int main()
{
    int m = 100, i, len = 100000000;// for 10 ^ 8 takes 8 sec
    int val[6*m];
    random(len);
    val[1] = 1;
    LLU t;
    for( i = 2; i <= 6 * m; i++)
    {
        val[i] = (val[i-1] +  val[i-2]) % m;
        if(  val[i] == 1 && val[i-1] == 0)
            break;
    }
    LLU nmodp = mod(n, len, i);
    printf("%d",val[nmodp]);
	return 0;
}

