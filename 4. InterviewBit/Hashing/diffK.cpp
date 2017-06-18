int Solution::diffPossible(const vector<int> &A, int B) {
    int  n = A.size();
    if( n == 0)
        return 0;
    unordered_map <int, int> um;
    for( int i = 0; i < n; i++){
        int x = A[i];
        int val1 = B + x;
        int val2 = x - B;
        if( um.find(val1) != um.end() || um.find(val2) != um.end())
            return 1;
        um[x] = i;
    }
    return 0;
}
