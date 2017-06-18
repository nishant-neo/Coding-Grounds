#include <iostream>
#include <vector>
using namespace std;
vector<vector<int> > generate(int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    vector<vector<int> > res;
    vector <int> temp;
    temp.push_back(1);
    res.push_back(temp);
    for( int i = 2; i <= A; i++)
    {

        vector <int> temp;
        for( int k = 0; k < i; k++)
        {
            //cout<<k<<endl;
            int t1 = 0, t2 = 0;
            if( k-1 >= 0)
                t1 = res[i-2][k-1];
            if( k <= i-2)
                t2 = res[i-2][k];
            temp.push_back(t1+t2);
        }
        //cout<<"GFG"<<i<<endl;
        //cout<<endl<<"***";
        for( int k = 0; k < i; k++)
        {
            cout<<temp[k]<<" ";
        }
        cout<<endl;
        res.push_back(temp);
    }
    cout<<res.size()<<endl;
    return res;
}
int main()
{
    vector<vector<int> > x = generate(5);
    for( int i = 0; i < x.size(); i++)
    {

        for( int k = 0; k < x[i].size(); k++)
        {
            cout<<x[i][k]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
