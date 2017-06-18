int Solution::maxArr(vector<int> &A) {
    int n = A.size();

    vector <int> C(n);
    vector <int> B(n);

    for( int i = 0; i < n; i++){
        B[i] = A[i] + i;
        C[i] = A[i] - i;
    }

    int max1 = INT_MIN, max2 = INT_MIN, min1 = INT_MAX, min2 = INT_MAX;
    for( int i = 0; i < n; i++){
        max1 = max( max1, B[i]);
        min1 = min( min1, B[i]);
        max2 = max( max2, C[i]);
        min2 = min( min2, C[i]);
    }
    return max ( abs(max1 - min1), abs(max2 - min2) );
}
