#include<stdio.h>
int main()
{
	int t,n, i;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d", &n);
	    int A[n+1];
	    int max[n+1];
	    int min[n+1];
	    for( i = 1; i <= n; i++){
	        scanf("%d", &A[i]);
	    }
	    max[1] = 1, min[1] = 1;
	    if( A[1] > 0)
	        max[1] = A[1];
	    else if( A[1] < 0)
	        min[1] = A[1];
	    for( i = 2; i <= n; i++)
	    {
	        if( A[i] > 0){
	            max[i] = A[i] * max[i-1];
	            min[i] = A[i] * min[i-1];}
	       else if( A[i] < 0){
	        	max[i] = A[i] * min[i-1];
	            min[i] = A[i] * max[i-1];}
	       else
	        {
	            max[i] = 1, min[i] = 1;
	        }
	        max[i] = max[i] < 0 ? 1:max[i];
	        min[i] = min[i] > 0 ? 1:min[i];
	        //printf("%d %d\n",min[i],max[i]);

	    }
	    int m = -1;
	    /*for( i = 1;i <=n; i++)
	    {
	        if( m < max[i])
	            m = max[i];
	    }*/
	    printf("%d\n",m);
	}

}
