bool ispalindrome(string A, int l, int r){
    while( l < r){
        while( l < r && !isalnum(A[l]))
            l++;
        while( l < r && !isalnum(A[r]))
            r--;
        if( toupper(A[l]) != toupper(A[r]) )
            return 0;
        l++;
        r--;
    }
    return 1;
}
void partitionHelper(string A, int start, int end, vector<vector<string> > &res, vector <string> ans) {
    if (start >= end)
    {
        res.push_back(ans);
        return;
    }

    for (int i=start; i<end; i++)
    {
        if (ispalindrome(A, start, i))
        {
            ans.push_back(A.substr(start, i-start+1));
            partitionHelper(A, i+1, end, res, ans);
            ans.pop_back();
        }
    }
}
vector<vector<string> > Solution::partition(string A) {
    vector<vector<string> > res;
    vector<string> ans;
    partitionHelper(A, 0, A.size(), res, ans);
    sort( res.begin(), res.end());
    return res;
}
