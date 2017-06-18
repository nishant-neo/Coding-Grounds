vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    unordered_map <string, vector<int> > um;
    int n = A.size();
    for( int i = 0; i < n; i++ ){
        string strSorted(A[i]);
        sort( strSorted.begin(), strSorted.end());
        um[strSorted].push_back(i+1);
    }
    vector< vector<int> > res;

    for( unordered_map<string,vector<int> >::iterator it = um.begin(); it!=um.end(); ++it){
        res.push_back(it->second);
    }
    return res;
}

