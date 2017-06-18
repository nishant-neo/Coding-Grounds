vector<vector<int> > Solution::diagonal(vector<vector<int> > &A) {
    int length = A.size();
    int n = 2 * length - 1;
    vector< vector <int> > res;
    for( int i = 0 ; i < n; i++){
        vector<int> temp;
        res.push_back(temp);
    }
    for( int i = 0 ; i < length; i++)
    {
        for( int j = 0; j < length; j++)
        {
            res[i+j].push_back(A[i][j]);
        }
    }
    return res;
}
