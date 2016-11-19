#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>
#define ll long long int
#define LEN 1000
#define HASHLEN 2000
#define P 1009//49390927

using namespace std;

class PHNode{
public:
    ll a;
    ll b;
    vector <ll> secH;
    ll n;
} ;
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
    return ((((a% P)*(x % P))% P + (b % P)) % P) % m;//changes to be made in case the prime number to be taken is nery large
}
void secondaryHash(ll a, ll b, vector <ll> &numbers, vector <PHNode> &PHList)
{
    int flag;
    ll x, temp, temp2, temp3;
    for( int i = 0 ; i < LEN; i++){
        x = numbers[i];
        temp = hashF(a,b,x,HASHLEN);
        if(PHList[temp].a==-1){
			PHList[temp].a = random(5)%117;;
			PHList[temp].b = random(5);;
		}
        temp2 = hashF(PHList[temp].a, PHList[temp].b, x, PHList[temp].secH.size() );
        if(PHList[temp].secH[temp2] == -1){
            PHList[temp].secH[temp2] = x;
        }
        else if( PHList[temp].secH[temp2] == x)
            continue;

        else{
            cout<< "Finding a & b for bin = "<< temp<< endl;
            /*for( int j = 0; j < PHList[temp].secH.size(); j++){
                     if( PHList[temp].secH[j] == -1)
                            PHList[temp].secH[j] = x;
                }*/

            while(1){
                flag = 0;
                vector <ll> tempNode( (PHList[temp].n *PHList[temp].n) , -1 );
                ll tempA = random(5)%117;
                ll tempB = random(5);
                cout<< tempA<<" "<<tempB<<endl;
                for( int j = 0; j < (PHList[temp].n *PHList[temp].n) ; j++)
                {

                    if( PHList[temp].secH[j] != -1)
                    {
                        temp3 = hashF(tempA, tempB, PHList[temp].secH[j], (PHList[temp].n *PHList[temp].n)  );
                        if( tempNode[temp3] == -1){
                            tempNode[temp3] = PHList[temp].secH[j];
                        }
                        /*else if( tempNode[temp3] == PHList[temp].secH[j] )
                            continue;*/
                        else{
                            cout<<tempNode[temp3]<<"   "<<PHList[temp].secH[j]<<" "<<temp3<<endl;
                            flag = 1;break;
                        }
                    }
                }
                if(flag==1)
					continue;
                else{
                        cout<<"FDFD";
                    PHList[temp].secH = tempNode;
                    PHList[temp].a = tempA;
                    PHList[temp].b = tempB;
                    break;
                }
            }
            cout<<"Success!!\n";


        }
    }
}

void primaryHash(vector<ll> &numbers, vector<PHNode> &PHList)
{
    ll a, b, sum;
    int flag = 0;
    for(int i = 0; i < HASHLEN; i++){
			PHList[i].n=0;
    }
    while(1){
        sum = 0;
        a = random(5)%117;
        b = random(5);
        cout<<a<<" and "<<b<<endl;
        for( int i = 0 ; i < LEN; i++){
            ll temp = hashF(a,b,numbers[i] ,HASHLEN);
            (PHList[temp].n) += 1;

        }
        for( int i = 0 ; i < HASHLEN; i++){
            sum = sum + (PHList[i].n * PHList[i].n);
        }
        if( sum < HASHLEN){
            cout<<"RRRR"<<endl;break;}
    }
    for( int i = 0; i < HASHLEN; i++){
        vector <ll> temp(PHList[i].n*PHList[i].n, -1);
        PHList[i].a = -1, PHList[i].b = -1;
        PHList[i].secH = temp;
    }
    cout << "Rows in the 2d vector: " << PHList.size();
    for( int i = 0; i < 2*LEN; i++){
        cout << "Columns in the 1st row: " << PHList[i].n<<" "<< PHList[i].secH.size() << endl;
    }
    secondaryHash( a, b, numbers, PHList);
}

int main()
{
    vector <ll> numbers(LEN);
    vector <PHNode> PHList(HASHLEN);
    srand(time(NULL));
    for( int i = 0; i < LEN; i++){
        numbers[i] = random(10);
//        cout<<numbers[i]<<endl;
    }
    primaryHash(numbers, PHList);
    for(int i = 0; i < HASHLEN; i++){
		cout<< PHList[i].n << " : ";
		if(PHList[i].n > 0){
			for(int j = 0; j < PHList[i].secH.size() ;j++)
				cout<< PHList[i].secH[j]<< " ";
		}
		cout<< endl;
	}
}
