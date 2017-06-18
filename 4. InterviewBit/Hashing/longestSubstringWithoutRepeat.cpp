int Solution::lengthOfLongestSubstring(string A) {
    int n = A.size();
    if( n <= 1)
        return n;

    unordered_map<char,int> um;

    int s = 0, e = 0, max = INT_MIN;
    for( int i = 0; i < n; i++){
        if( um.find(A[i]) == um.end()){
            um[A[i]]++;
            e = i;
            if( max < (e-s+1)){
                //cout<<s<<" "<<e<<endl;
                max = e-s+1;
            }
        }
        else{
            //cout<<s<<"*"<<i<<endl;
            while( s < i && (um.find(A[i]) != um.end()) ){
                um[A[s]] -- ;
                if( um[A[s]] <= 0)
                    um.erase(A[s]);
                s++;
            }
            //cout<<s<<"*"<<i<<endl;
            //s = s - 1;
            i = i - 1;
        }
    }
    return max;
}

