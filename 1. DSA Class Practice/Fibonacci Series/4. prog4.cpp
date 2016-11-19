#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#define M 100

using namespace std;
int arr[1000000];
int getrand(int min, int max) {
  static bool init = false;

  if (!init) {
    srand(time(NULL));
    init = true;
  }

  return rand()%(max-min)+min;
}

void Multiply(int A[][2], int B[][2]) {
    int C[2][2];
	C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0];
	C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1];
	C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0];
	C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1];
	A[0][0] = (C[0][0])%M;
	A[0][1] = (C[0][1])%M;
	A[1][0] = (C[1][0])%M;
	A[1][1] = (C[1][1])%M;
}

void pow(int * arr, int size, int B[][2],int X[][2])
{
    if(size==-1)
          return;
    if(size>=0)
    {
        int Y[2][2];
        Y[0][0] = B[0][0];
        Y[0][1] = B[0][1];
        Y[1][0] = B[1][0];
        Y[1][1] = B[1][1];
        for(int i = 0;i<arr[size]-1;i++)
            Multiply(Y,B);
        B[0][0] =  Y[0][0];
        B[0][1] =  Y[0][1];
        B[1][0] =  Y[1][0];
        B[1][1] =  Y[1][1];
        if(arr[size]!=0)
            Multiply(X,B);
        int Y1[2][2];
        Y1[0][0] = B[0][0];
        Y1[0][1] = B[0][1];
        Y1[1][0] = B[1][0];
        Y1[1][1] = B[1][1];
        for(int i = 0;i<9;i++)
            Multiply(B,Y);
        size--;
        pow( arr,size,B,X);
       }
}

int main()
{
    int n;
    int A,y,i;
    int B[2][2] = {{1,1},{1,0}};;
    int X[2][2] = {{1,0},{0,1}};;
    y= 1;
    cin>>n;
    for( i=0;i<n;i++)
        arr[i] = getrand(0,9);
    int size = n-1;
    pow( arr,size,B,X);
    cout<<X[1][0]<<"\n";
    return 0;

}
