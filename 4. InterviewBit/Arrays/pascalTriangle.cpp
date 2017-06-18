vector<vector<int> > Solution::generate(int A) {
    vector<vector<int> > res;
    if( A == 0)
        return res;
    vector <int> temp;
    temp.push_back(1);
    res.push_back(temp);
    for( int i = 2; i <= A; i++){
        vector <int> temp;
        temp.push_back(1);
        for( int k = 1; k < res[i-2].size(); k++)
            temp.push_back( res[i-2][k-1] + res[i-2][k]);
        temp.push_back(1);
        res.push_back(temp);
    }
    return res;
}
