#include <stdio.h>

#include <sys/types.h>

#include <unistd.h>

void zrand(void);



int main(){

zrand();

}



void zrand(void){

int rnd, i;

srand(getpid());

for( i = 0; i < 10; i++) {

rnd = (rand()%1000);

printf("%d ",rnd);

}

}
