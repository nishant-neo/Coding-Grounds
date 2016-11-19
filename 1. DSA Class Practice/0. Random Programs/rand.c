#include<stdio.h>

#include<sys/time.h>

#include<math.h>

#define max 179424673

double getTime(int);

main()

{

double start,stop,elapsedTime;

int n;

long int count=0,cnt=0,i,j,k;

static long int prime[max],p=2;

start=getTime(-6);

printf("%lf\n",start);

prime[0]=prime[1]=1;

for( j = 2; j <= max + 1; j++)

{

if(prime[j] == 0)

{

i=j;

for(k = 2*i; k <= max + 1; k = k + i)

{

prime[k] = 1;

}

}

}

for(p = 2; p < max + 1; p++)

{

if(prime[p] == 0)

{

count++;

}

}

stop = getTime(-6);

elapsedTime = stop - start;

printf("Elapsed Time: %lf\n",elapsedTime);

printf("Count: %ld\n",count);

}

double getTime(int n)

{

double time;

struct timeval tv;

gettimeofday(&tv,NULL);

printf("%d\n", n);

time=(tv.tv_sec * pow(10,6) + tv.tv_usec ) / pow(10, 6 + (-6));

return time;

}
