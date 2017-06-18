void combineHelper(int n, int start, int k, vector <vector<int> > &res, vector<int> ans ) {
    if( ans.size() == k){
        res.push_back(ans);
        return;
    }
    if( start == n+1)
        return;

    combineHelper( n, start+1, k, res, ans );
    ans.push_back( start);
    combineHelper( n, start+1, k, res, ans );
}
vector<vector<int> > Solution::combine(int n, int k) {
    vector <vector<int> > res;
    vector<int> ans;
    if( n < k)
        return res;
    combineHelper( n, 1, k, res, ans);
    sort( res.begin(), res.end() );
    return res;
}
