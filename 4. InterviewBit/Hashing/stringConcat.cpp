bool check( unordered_map <string,int> &um ){
    for(unordered_map <string,int>::iterator it = um.begin(); it != um.end(); ++it )
        if( it -> second != 0)
            return 0;
    return 1;
}
vector<int> Solution::findSubstring(string A, const vector<string> &B) {
    vector <int> res;
    int n = B[0].size();
    int n2 = B.size();
    int n3 = A.size();
    if( n3 < n2*n)
        return res;
    unordered_map <string,int> um;

    for( int i = 0; i < B.size(); i++)
        um[B[i]] += 1;

    int start, end;
    for( start = 0; start <= (A.size()- n*B.size()); start++){
        string t = A.substr(start, n);
        int save = start;
        if( um.find(t) == um.end())
            continue;
        else{
            while(um.find(t) != um.end() && start < A.size()){
                um[t]--;
                if( um[t] < 0)
                    break;
                start += n;
                t = A.substr(start, n);
                if( check( um )){
                    res.push_back(save);
                    break;
                }
            }
            start = save;
            um.clear();
            for( int i = 0; i < B.size(); i++)
                um[B[i]] += 1;
        }
    }
    return res;
}
