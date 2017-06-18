vector<int> Solution::plusOne(vector<int> &A) {
    int n = A.size();

    int l = 0;
    while( A[l] == 0)
        l++;

    vector <int> res;

    int carry = 1;
    for( int i = n-1; i >= l; i--){
        res.push_back( (carry + A[i]) % 10 );
        carry = (carry + A[i]) / 10;
    }
    if( carry )
        res.push_back(1);

    reverse( res.begin(), res.end());
    return res;
}
