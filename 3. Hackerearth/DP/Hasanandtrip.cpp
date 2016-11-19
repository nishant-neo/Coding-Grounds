#include <stdio.h>
#include <math.h>
#include <float.h>
double max(double a, double b)
{
    return a > b? a:b;
}
double eucledian( int a, int b, int c, int d)
{
    return sqrt( abs((a-c)*(a-c) + (b-d)*(b-d)));
}
int main()
{
    int n, i, j, val ;
    scanf("%d", &n);
    int x[n+1], y[n+1], f[n+1];
    for( i = 1; i <= n; i++)
        scanf("%d %d %d", &x[i], &y[i], &f[i]);
    long double dist[n+1];
    dist[1] = f[1];
    for( i = 2; i <= n; i++){
            dist[i]= -1ll<<60;
        for( j = 1; j < i; j++)
        {
            dist[i] = max( dist[i], dist[j]- eucledian(x[i], y[i], x[j], y[j]));
        }
        dist[i] += f[i];
        printf("%f\n",dist[i]);
    }
    printf("%.6f\n",dist[n]);
    return 0;
}
