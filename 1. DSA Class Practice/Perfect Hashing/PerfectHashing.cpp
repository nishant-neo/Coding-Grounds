#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>
#define ll long long int
#define LEN 100
#define HASHLEN 200
#define P 5915587277
using namespace std;

ll numbers[LEN];
ll n[LEN*2];
ll random(int len)
{
    ll x = 0;
    for( int i = 0; i < len; i++)
    {
       x = x*10 +  ((rand() % 9)+1);
    }
    return x;
}
ll hashF(ll a, ll b, ll x, ll m)
{
    return ((a*x + b) % P) % m;//changes to be made in case the prime number to be taken is nery large
}
int main()
{
    ll a, b;
    srand(time(0));
    for( int i = 0; i < LEN; i++){
        numbers[i] = random(10);
        //cout<<numbers[i]<<endl;
    }
    int flag = 0;
    while(!flag){
        flag = 1;
        a = random(2);
        b = random(3);
        cout<<a<<" "<<b;
        for( int i = 0 ; i < LEN; i++){
            ll temp = hashF(a,b, i, HASHLEN);
            n[ temp ]++;
        }
        //cout<<"check"<<endl;
        for( int i = 0; i < HASHLEN; i++){
            if( (n[i] * n[i]) >=  2*LEN)
                flag = 0;
        }
    }

    vector<vector<ll> > PHash;
    for( int i = 0; i < HASHLEN; i++){
        vector <ll> temp(n[i]*n[i]);
        PHash.push_back(temp);
    }
    cout << "Rows in the 2d vector: " << PHash.size();
    for( int i = 0; i < 2*LEN; i++){
        cout << "Collumns in the 1st row: " << n[i]<<" "<< PHash[i].size() << endl;
    }
    flag = 0;
    while(!flag){
        flag = 1;
        a = random(2);
        b = random(3);
        cout<<a<<" "<<b;

        for( int i = 0 ; i < LEN; i++){
            ll x = numbers[i];
            cout<<"chevk0\n";
            ll temp = hashF(a,b,x,HASHLEN);
            cout<<temp<<"chevk01\n";
            cout<<PHash[temp].size()<<endl;
            ll temp2 = hashF(a,b,x,PHash[temp].size() );
            cout<<"chevk1\n";
            if(PHash[temp][temp2] != 0){
                cout<<"Collision"<<endl;flag = 0;break;
            }
            cout<<"chevk2\n";
            PHash[temp][temp2] = numbers[i];
            cout<<"chevk3\n";
        }
    }
    for (int i = 0; i < PHash.size(); i++)
    {
        for (int j = 0; j < PHash[i].size(); j++)
        {
            cout << PHash[i][j]<<" " ;
        }
        cout<<endl;
    }


}
