int Solution::maxSubArray(const vector<int> &A) {
    int n = A.size();

    long long int sum = 0, maxSum = INT_MIN;
    for( int i = 0; i < n; i++){
        sum += A[i];
        maxSum = max( maxSum, sum);
        if( sum < 0){
            sum = 0;
        }
    }
    return maxSum;
}
