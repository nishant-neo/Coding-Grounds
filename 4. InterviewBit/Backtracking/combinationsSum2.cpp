void combinationSumHelper(vector<int> &A, int start, int B, vector<vector<int> > &res, vector<int> ans) {
    if( B == 0){
        if( res.size() == 0 || ans.size() != res[res.size()-1].size())
            res.push_back(ans);
        else{
            int i;
            for( i = 0; i < ans.size(); i++)
                if( res[res.size()-1][i] != ans[i])
                    break;
            if( i != ans.size())
                res.push_back(ans);
        }

        return;
    }
    if( start == A.size() || B < 0)
        return;
    combinationSumHelper(A, start + 1, B, res,  ans);
    ans.push_back(A[start]);
    combinationSumHelper(A, start + 1, B - A[start], res,  ans);
}
vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    vector<vector<int> > res;
    vector<int> ans;
    sort( A.begin(), A.end());
    combinationSumHelper(A, 0, B, res, ans);
    sort( res.begin(), res.end());
    return res;

}

