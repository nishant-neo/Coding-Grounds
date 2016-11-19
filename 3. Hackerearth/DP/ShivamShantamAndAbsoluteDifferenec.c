#include <stdio.h>
#include <math.h>

int main()
{
    int n, i, q, count;
    long long unsigned int sumA = 0, sumB = 0;
    scanf("%d",&n);
    int A[n], B[n];
    for( i = 0; i < n; i++){
        scanf("%d", &A[i]);
        sumA += A[i];
    }
    for( i = 0; i < n; i++){
        scanf("%d", &B[i]);
        sumB += B[i];
    }
    scanf("%d",&q);
    while(1)
