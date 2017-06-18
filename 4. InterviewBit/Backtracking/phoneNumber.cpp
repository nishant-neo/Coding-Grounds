vector<string> Solution::letterCombinations(string A) {
    string encod[] = {"0","1", "abc", "def", "ghi","jkl", "mno", "pqrs", "tuv", "wxyz"};
    int n = A.size();
    vector <string> res;
    if( n == 0)
        return res;
    //cout<<encod[(int)(A[0] - '0')][0];

    for( int i = 0; i < encod[(int)(A[0] - '0')].size(); i++){
        string s = "";
        s += encod[(int)(A[0] - '0')][i];;
        res.push_back( s);
    }

    for( int i = 1; i < n; i++){
        vector <string> res2;
        for( int k = 0; k < res.size(); k++){
            for( int j = 0; j < encod[(int)(A[i] - '0')].size(); j++){
                string s = "";
                s += res[k];
                s += encod[(int)(A[i] - '0')][j];
                res2.push_back(s);
            }
        }
        res2.swap(res);
    }

    return res;

}

