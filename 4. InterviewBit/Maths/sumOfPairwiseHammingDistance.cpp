int Solution::hammingDistance(const vector<int> &A) {
    int n = A.size();
    long long int ans = 0;
    for( int i = 0; i < sizeof(int) * 8; i++)
    {
        long long int count = 0;
        for( int j = 0; j < n; j++)
        {
            if( A[j] & (1 << i) )
                count++;
        }
        ans =  (ans + ( ( count * (n - count) ) %  1000000007) ) % 1000000007 ;
    }
    return (int)(2 * ans) % 1000000007;
}
