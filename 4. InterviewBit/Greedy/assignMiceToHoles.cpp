int Solution::mice(vector<int> &A, vector<int> &B) {
    int n = A.size();
    sort( A.begin(), A.end());
    sort( B.begin(), B.end());

    int maxVal = INT_MIN;
    for( int i = 0 ; i < n; i++){
        maxVal = max( maxVal ,abs(A[i]- B[i]) );
    }

    return maxVal;
}
