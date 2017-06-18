void subsetshelper(vector<int> &A, int start ,vector<vector<int> > &res, vector <int> ans ) {
    if( start == A.size())
        return;
    subsetshelper(A, start+1, res, ans );
    ans.push_back(A[start]);
    res.push_back(ans);
    subsetshelper(A, start+1, res, ans );
}
vector<vector<int> > Solution::subsets(vector<int> &A) {
    int n = A.size();
    vector<int>ans;
    vector<vector<int> > res;
    res.push_back(ans);
    if( n == 0)
        return res;
    sort( A.begin(), A.end());
    subsetshelper(A, 0, res, ans);
    sort(res.begin(), res.end());
    return res;

}

