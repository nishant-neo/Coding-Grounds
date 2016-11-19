#include <stdio.h>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
int ED( char* s1, char* s2, int m, int n){
    if( m == 0 || n == 0)
        return MAX( m, n);
    else if( s1[m-1] == s2[n-1])
        return ED( s1, s2, m-1, n-1);
    else
        return 1 + MAX(MAX (ED( s1, s2, m-1, n-1),ED( s1, s2, m-1, n)), ED( s1, s2, m, n-1));
}
int ED_DP( char* s1, char* s2, int m, int n){
    int i, j ;
    int EDM[m+1][n+1];
    for( i = 0; i <= m; i++){
        for( j = 0; j <= n; j++){
            if( i == 0)
                EDM[i][j] = j;
            else if( j == 0)
                EDM[i][j] = i;
            else if( s1[i-1] == s2[j-1])
                EDM[i][j] = EDM[i-1][j-1];
            else
                EDM[i][j] = 1 + MIN( (MIN( EDM[i-1][j], EDM[i][j-1])) , EDM[i-1][j-1]);
        }
    }
    printf("%d\n",EDM[m][n]);

}
int main() {
	int t, m, n ;
	scanf("%d", &t);
	while( t-- ){
	    scanf("%d %d", &m, &n);
	    char s1[m];
	    char s2[n];
	    scanf("%s", s1);
	    scanf("%s", s2);
	    //printf("%d\n",ED( s1, s2, m, n));
	    ED_DP( s1, s2, m, n);
	}
	return 0;
}
