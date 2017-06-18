
vector<int> Solution::plusOne(vector<int> &A)
{
    int length = A.size();
    int carry = 1, sum;
    vector<int> res;
    for( int i = length-1; i >= 0; i--)
    {
        sum = (A[i] + carry) % 10;
        carry = (A[i] + carry) / 10;
        res.push_back(sum);
    }
    if( carry == 1)
        res.push_back(carry);
    reverse(res.begin(), res.end());
    int flag = 1;
    vector <int> r;
    for( int i = 0; i < res.size(); i++)
    {
        if ( flag && res[i] == 0)
            continue;
        if( res[i] != 0 && flag)
            flag = 0;
        r.push_back(res[i]);
    }
    return r;
}
