#include <stdio.h>
#define MAX(a,b) a>b? a:b

int main() {
    int t, n, i, j;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        int arr[n];
        int lis[n];
        for( i = 0; i < n; i++)
            scanf("%d",&arr[i]);
        lis[0] = 1;
        for( i = 1 ; i < n; i++ )
        {
            lis[i] = 1;
            for( j = i; j >= 0; j--)
            {
                if( arr[j] < arr[i])
                    lis[i] = MAX( lis[i], lis[j] + 1);
            }
        }
        int max = 0;
        for( i = 0; i < n; i++)
        {
            if(  max < lis[i])
                max = lis[i];
        }
        printf("%d\n",max);
    }
	return 0;
}
