#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
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

void Multiply(int mat1[][2], int mat2[][2]) {


    int mat3[2][2] = {};
for (int r = 0; r < 2; r++) {
    for (int c = 0; c < 2; c++) {
        for (int in = 0; in < 2; in++) {
            mat3[r][c] = (mat3[r][c]%100 + mat1[r][in] * mat2[in][c]%100)%100;
        }

    }

}

    for (int r = 0; r < 2; r++)
    {
        for (int c = 0; c < 2; c++)
        {
           mat1[r][c] = mat3[r][c];
            }
    }

}


void pow_in_arr(int * arr, int size, int B[][2],int X[][2])
    {
      if(size==-1)
          {
          return;
          }
       if(size>=0)
           {//cout<<X[1][0]<<"\n";
               int Y[2][2];
                Y[0][0] = B[0][0];
                Y[0][1] = B[0][1];
                Y[1][0] = B[1][0];
                Y[1][1] = B[1][1];
           for(int i = 0;i<arr[size]-1;i++)
               {

                     Multiply(Y,B);
                   //cout<<Y[1][0]<<"\n";
               //cout<<B[0][0]<<"\n";
               }
                  B[0][0] =  Y[0][0];
                  B[0][1] =  Y[0][1];
                  B[1][0] =  Y[1][0];
                  B[1][1] =  Y[1][1];
           //cout<<B[1][0]<<"\n";

                     if(arr[size]!=0)
                   Multiply(X,B);
               //cout<<X[1][0]<<"\n";
           int Y1[2][2];
                Y1[0][0] = B[0][0];
                Y1[0][1] = B[0][1];
                Y1[1][0] = B[1][0];
                Y1[1][1] = B[1][1];
           for(int i = 0;i<9;i++)
               {


                     Multiply(B,Y);
                     //cout<<B[1][0]<<"\n";
               }

                   size--;
           pow_in_arr( arr,size,B,X);

       }

}


int main()
{
     int n;
    int A,y,i;
    int B[2][2];
    int X[2][2];
    y= 1;
    X[0][0] = 1;
    X[0][1] = 0;
    X[1][0] = 0;
    X[1][1] = 1;
    B[0][0] = 1;
    B[0][1] = 1;
    B[1][0] = 1;
    B[1][1] = 0;
    cin>>n;
    for( i=0;i<n;i++)
         {
         arr[i] = getrand(0,9);

        //  cout<<arr[i];

         }

       int size = n-1;
       cout<<"\n";
      pow_in_arr( arr,size,B,X);
      cout<<X[1][0]<<"\n";
    return 0;

}
