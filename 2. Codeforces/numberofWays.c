#include <stdio.h>

int main()
{
    long long int n, c1 = 0, c2 = 0, i;
    long long int sum = 0, bin;
    scanf("%d",&n);
    int A[n];
    for( i = 0; i < n; i++){
        scanf("%d",&A[i]);
        sum = sum +A[i];
    }
    bin = sum / 3;
    sum = 0;
    if(bin>0){
    for( i = 0; i < n; i++){
        sum+= A[i];
        if(  sum%bin == 0 && sum / bin == 1 )
            c1++;
        else if( sum%bin == 0 && sum / bin == 2 )
            c2++;
    }sum=c1*c2;}
    else{
        for( i = 0; i < n; i++){
            sum+= A[i];
            if( sum == 0)
            c1++;
        }
        c1--;
        sum = ((c1-1)* c1)/2;
    }
    printf("%d\n", sum);

    return 0;
}
