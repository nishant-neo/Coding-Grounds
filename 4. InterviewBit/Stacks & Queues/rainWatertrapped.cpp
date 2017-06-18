#define MIN(a,b) a <= b ? a : b
int Solution::trap(const vector<int> &A) {
    int n = A.size();
    if( n <= 2)
         return 0;
    vector <int> LMax(n,-1);
    vector <int> RMax(n,-1);
    for( int i = 1; i < n ; i++){
        if( i == 1 || A[i-1] >= A[LMax[i-1]] )
            LMax[i] = i-1;
        else
            LMax[i] = LMax[i-1];
    }
    for( int i = n-2; i >= 0; i--){
        if( i == n-1 || A[i+1] >= A[RMax[i+1]] )
            RMax[i] = i+1;
        else
            RMax[i] = RMax[i+1];
    }
    int res = 0;
    for( int i = 1; i < n-1; i++){
        int mine = MIN( A[LMax[i]], A[RMax[i]]);
        if( mine - A[i] > 0)
            res += (mine - A[i]);
    }
    return res;
}
