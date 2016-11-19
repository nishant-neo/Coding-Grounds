#include <stdio.h>


int count[10010];
int main()
{
	int t, n, x, i, j;
	scanf("%d", &t);
	while( t --){
	scanf("%d %d", &n, &x);
	int A[n+1];
	int used[n+1];
	long long int s = 0;
	for( i = 0; i < n; i++){
		scanf("%d",&A[i]);
		s = s + A[i];
	}
	int count[s+5];
	count[0] = 1;
	int sum = 0;
	for( i = 0; i < n; i++){

		for( j = 0; j <= sum; j++)
		{
			//printf("%d %d\n",j,count[j]);
			if( count[j] >= 1){
				count[j+A[i]] += 1;
				//printf("$$$%d %d %d %d\n",A[i],j+A[i],count[j+A[i]],sum);
			}
		}
		sum += A[i];
	}
	//print
	if( x > sum || count[x] >= 2)
		printf("YES\n");
	else
		printf("NO\n");
	}




}

