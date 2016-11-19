#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t, i;

	cin>>t;
	while( t--){
		string s;
		cin>>s;
		char last = s[0];
		cout<<last;
		for( i = 1; i < s.size(); i++)
		{
			if( last == s[i])
				continue;
			else
				{
					last = s[i];
					cout<<last;
				}
		}
		cout<<endl;
	}

    return 0;
}
