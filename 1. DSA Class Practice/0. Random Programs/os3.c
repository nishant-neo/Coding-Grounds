#include<stdio.h>

#include<sys/time.h>

#include<math.h>



double getTime(int);



int main(){

double start,stop,elapsedTime;

int i,j,precision;

printf("Enter precision value:");

scanf("%d",&precision);

start=getTime(precision);

for(i=0;i<2000000000;i++);

stop=getTime(precision);

elapsedTime=stop-start;

printf("%lf\n",elapsedTime);

}



double getTime(int x) {

double time;

struct timeval tv;

gettimeofday(&tv,NULL);

time=tv.tv_sec*pow(10,x);

return time;

}
