void combinationSumHelper(vector<int> &A,int start, int B, vector<vector<int> > &res, vector<int> ans) {
    if( B < 0)
        return;
    if( B == 0  ){
        res.push_back(ans);
        return;
    }
    if(  start == A.size() )
        return;
    combinationSumHelper(A, start + 1, B, res, ans);
    ans.push_back(A[start]);
    combinationSumHelper(A,start , B - A[start], res, ans);
    //combinationSumHelper(A,start, B - A[start], res, ans);
    ans.pop_back();
}
vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    vector<vector<int> > res;
    vector<int> ans;
    vector<int> b;
    sort( A.begin(), A.end());
    b.push_back(A[0]);
    for(int i=1;i<A.size();i++){
      if(A[i]!=b[b.size()-1])
        b.push_back(A[i]);
    }
    combinationSumHelper( A, 0, B, res, ans);
    sort(res.begin(), res.end());
    return res;
}

