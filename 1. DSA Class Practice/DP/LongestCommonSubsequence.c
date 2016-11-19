#include <stdio.h>
#define MAX(a,b) a>b?a:b

int main() {
    int t, m, n, i, j;
    scanf("%d",&t);
    while( t--)
    {
        scanf("%d %d", &m, &n);
        char s1[m+1];
        char s2[n+1];
        scanf("%s", s1);
        scanf("%s", s2);
        int LCS[m+2][n+2];
        for( i = 0; i < m+2; i++)
            LCS[i][0] = 0;
        for( j = 0; j < n+2; j++)
            LCS[0][j] = 0;
        for( i = 1; i <= m; i++){
            for( j = 1; j <= n; j++){
                if( s1[i-1] == s2[j-1])
                    LCS[i][j] = LCS[i-1][j-1] + 1;
                else
                    LCS[i][j] = MAX( LCS[i-1][j], LCS[i][j-1]);
            }
        }
        printf("%d\n",LCS[m][n]);

    }
	return 0;
}
