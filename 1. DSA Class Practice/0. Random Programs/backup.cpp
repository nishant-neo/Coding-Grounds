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

vector <ll> numbers(LEN);
vector <int> n(LEN*2);
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
void reHashF( ll a, ll b, vector< ll > &PHash,  vector< ll > &numbers, ll x)
{
    vector <ll> rehash;
    for( int t = 0; t < PHash.size(); t++)
    {
        if( PHash[t] != 0){
            rehash.push_back(PHash[t]);
        }
    }
    int old_len = PHash.size();
    rehash.push_back(x);
    int flag = 0;
    while(!flag)
    {
        flag = 1;
        PHash.resize(2*old_len);
        for( int t = 0; t < PHash.size(); t++ )
            PHash[t] = 0;
        for( int t = 0; t < rehash.size(); t++ )
        {
            ll temp2 = hashF(a,b,rehash[t],(PHash.size()) );
            if( PHash[temp2] != 0){
                flag = 0; break;
            }
            else
                PHash[temp2] = x;
        }
    }
}
void secondaryHash( ll a, ll b, vector< vector<ll> > &PHash,  vector< ll > &numbers)
{
    for( int i = 0 ; i < LEN; i++){
        ll x = numbers[i];
        ll temp = hashF(a,b,x,HASHLEN);
        ll temp2 = hashF(a,b,x,(PHash[temp].size()) );
        if(PHash[temp][temp2] != 0)
            {
                cout<<"collision\n";
                reHashF(a,b,PHash[temp], x)
                /**/

            }
        PHash[temp][temp2] = x;
    }
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
            ll temp = hashF(a,b, numbers[i], HASHLEN);
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
    secondaryHash(a,b,PHash,numbers);
    for (int i = 0; i < PHash.size(); i++)
    {
        for (int j = 0; j < PHash[i].size(); j++)
        {
            cout << PHash[i][j]<<" " ;
        }
        cout<<endl;
    }


}

