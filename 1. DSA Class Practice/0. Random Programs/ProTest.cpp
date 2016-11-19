#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <cmath>
#define ll long long int
#define LEN 100
using namespace std;
ll numbers[LEN+9];
ll num[36];
ll random(int len)
{
    ll x = 0;
    for( int i = 0; i < len; i++)
    {
       x = x*10 +  ((rand() % 9)+1);
    }
    return x;
}
ll couBits(ll x)
{
    //int num = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32678}
    //int num[32];
    ll ans = 0;
    for( int i = 0; i< 35; i++)
    {
        if( x & num[i] == num[i])
            ans = i;
    }
    return ans;
}
/*ll countBits(ll x)
{
    int bin[100];
    int count = 0;
    while( x )
    {
        bin[count] = x%2;
        x = x/2;
        count++;
    }
    return count;
}*/
ll countBits( ll x )
{
    ll count = 0;
    while( x )
    {
        x = x>>1;
        count++;
    }

    return count;
}
int main()
{
    srand(time(0));
    cout<<"Generating random Numbers:.... \n";
    for( int i = 0; i < LEN; i++){
        numbers[i] = random(2);
    }
    for( int i= 0; i< 35; i++)
        num[i] = pow(2,i);
    cout<<"Generated!!\n";
    ll count;
    for( int i = 0; i < LEN; i++)
    {
        cout<<numbers[i] << " : ";
        //int count = countBits(numbers[i]);
        //cout<< count-1 <<endl;//<<" "<<log(numbers[i])<<
        cout<<couBits(numbers[i])<<endl;

    }
    //cout<< count;


}
