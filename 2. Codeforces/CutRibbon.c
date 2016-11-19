#include <stdio.h>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b

int main()
{
    int n, i, j;
    int a[3];
    scanf("%d",&n);
    scanf("%d", &a[0]);
    scanf("%d", &a[1]);
    scanf("%d", &a[2]);
    int R[n+1];
    for( j = 0; j < n+1; j++)
        R[j] = -10000;
    R[0] = 0;
    for( i = 0; i < 3; i++){
        for( j = a[i]; j < n+1; j++)
        {
            R[j] = MAX( (R[j-a[i]] + 1), R[j] );
        }
    }
   /*for( j = 0; j < n+1; j++)
        {
            printf("%d\n",R[j]);
        }*/
    printf("%d\n",R[n]);
    return 0;

}
