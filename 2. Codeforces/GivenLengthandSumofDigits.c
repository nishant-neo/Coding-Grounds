#include <stdio.h>
#include <math.h>
int power( x )
{
    if( x == 0)
        return 1;
    return 10* power(x-1);
}
void findOut( int m, int s)
{
    int i, j;
    int Fmin[m+1][s+1];
    int Fmax[m+1][s+1];
    for( i = 0; i < m+1; i++){
        for( j = 0; j < s+1; j ++)
            Fmin[i][j] = -1;
            Fmax[i][j] = -1;
    }
    for( i = 1; i < m+1; i++){
        for( j = 1; j < s+1; j ++){
            if( j == 1 )
            {
                Fmin[i][j] = power(i-1);
                Fmax[i][j] = power(i-1);
                printf("!F[%d,%d] = %d %d\n",i, j, Fmin[i][j],Fmax[i][j]);
                continue;
            }
            if( j > 9*i )
                break;
            if( i == 1 && j < 10){
                Fmin[i][j] = j;
                Fmax[i][j] = j;
                printf("!F[%d,%d] = %d %d\n",i, j, Fmin[i][j],Fmax[i][j]);
                continue;
            }
            int k = j > 9 ? 9:j-1;
            while( j -k > 0 && Fmax[i-1][j-k] == -1 )
                k--;
            printf("^%d",k);
            Fmax[i][j] = power(i-1)*k + Fmax[i-1][j-k];

            k = 1;
            while( Fmin[i-1][j-k] == -1 )
                k++;
            Fmin[i][j] = power(i-1)*k + Fmin[i-1][j-k];
            printf("F[%d,%d] = %d %d\n",i, j, Fmin[i][j],Fmax[i][j]);
        }
        printf("%d %d\n",Fmin[i][j],Fmax[i][j]);
    }
    printf("%d %d\n",Fmin[m][s],Fmax[m][s]);


}
int main()
{
    int m,s ;
    scanf("%d %d", &m, &s);
    findOut( m, s);
    return 0;
}
