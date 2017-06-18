string Solution::longestPalindrome(string A) {
    int n = A.size();
    if( n == 1)
        return A;
    int maxVal = -1;
    string res = "";
    res += A[0];
    //cout<<res<<endl;
    for( int i = 0; i < n; i++){
        int l = i-1;
        int h = i;
        while( l >= 0 && h < n && A[l] == A[h]){
            if( (h-l+1) > maxVal){
                maxVal = h-l+1;
                res = A.substr(l, maxVal);
            }
            l--; h++;
        }

        l = i-1;
        h = i + 1;
        while( l >= 0 && h < n && A[l] == A[h]){
            if( (h-l+1) > maxVal){
                maxVal = h-l+1;
                res = A.substr(l, maxVal);
            }
            l--; h++;
        }
    }
    return res;
}
