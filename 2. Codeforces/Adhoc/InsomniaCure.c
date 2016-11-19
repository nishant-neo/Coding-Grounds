#include <stdio.h>

int main()
{
    int k, l, m, n, d, i, sum = 0;
    scanf("%d %d %d %d %d", &k,&l,&m,&n,&d);
    int check[d+1];
    for( i = 0; i < d+1; i++ )
        check[i] = 0;
    for( i = 1; i < d+1; i++)
    {
        if( (i % k == 0) || (i % l == 0) || (i % m == 0) || (i % n == 0)  )
            check[i] = 1;
    }
    for( i = 0; i < d+1; i++ )
        sum += check[i];
    printf("%d\n",sum);
    return 0;
}
