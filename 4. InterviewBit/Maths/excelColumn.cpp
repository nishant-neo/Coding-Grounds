int Solution::titleToNumber(string A) {
    int n = A.size();

    long long sum = 0;
    for( int i = 0; i < n; i++){
        sum = (sum * 26) +  (A[i] - 'A' + 1);
    }
    return sum;
}
