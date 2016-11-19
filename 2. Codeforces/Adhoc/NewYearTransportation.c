#include <stdio.h>

int main()
{
    int n, t, i;
    scanf("%d %d", &n, &t);
    int cell[n];
    for( i = 1; i < n; i++)
        scanf("%d", &cell[i]);
    i = 1;
    while(i < n)
    {
        i = i + cell[i];
        //printf("%d\n",i);
        if( i == t )
        {
            printf("YES\n");
            return 0;
        }
    }
    printf("NO\n");
    return 0;
}
