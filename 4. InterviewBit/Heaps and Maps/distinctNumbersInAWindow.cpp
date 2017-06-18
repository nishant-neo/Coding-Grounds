vector<int> Solution::dNums(vector<int> &A, int k) {
    vector <int> res;
    int n = A.size(), dcount = 0;
    if( n < k)
        return res;
    map <int, int> m;
    for( int i = 0; i < k; i++){
        if( m[A[i]] == 0 )
            ++dcount;
        m[A[i]] += 1;
    }
    res.push_back(dcount);
    for( int i = k; i < n; i++){
        if( m[A[i-k]] == 1)
            --dcount;
        m[A[i-k]] -= 1;
        if (m[A[i]] == 0)
            dcount++;
        m[A[i]] += 1;
        res.push_back(dcount);
    }
    return res;

}
