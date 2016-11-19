#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#define ll long long int
#define LEN 100
#define HASHLEN 200
#define P 5915587277
using namespace std;

ll numbers[LEN];
ll hashed[LEN*2];
ll random(int len)
{
    ll x = 0;
    for( int i = 0; i < len; i++)
    {
       x = x*10 +  ((rand() % 9)+1);
    }
    return x;
}
int main()
{
    ll a, b;
    srand(time(0));
    for( int i = 0; i < LEN; i++){
        numbers[i] = random(10);
        //cout<<numbers[i]<<endl;
    }
    while(1){
        a = random(2);
        b = random(3);
        cout<<a<<" "<<b;
        for( int i = 0 ; i < LEN; i++){
            ll temp = ((a*numbers[i] + b) % P) % HASHLEN;
            hashed[ temp ]++;
        }
        cout<<"check"<<endl;
        int flag = 1;
        for( int i = 0; i < HASHLEN; i++){
            if( (hashed[i] * hashed[i]) >=  2*LEN)
                flag = 0;
        }
        if( flag )
            break;
    }
    for( int i = 0; i < 2*LEN; i++){
        //numbers[i] = random(10);
        cout<<hashed[i]<<endl;
    }

}
