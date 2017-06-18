vector<int> Solution::maxset(vector<int> &A) {
    int n = A.size();

    long long sum = 0, maxSum = 0;
    int l = 0, lact = -1, ract = -2;
    for( int i = 0; i < n+1; i++){
        if( i == n || A[i] < 0  ){
            if( maxSum < sum || maxSum == sum && (ract-lact) < (i-1-l)
                                || maxSum == sum && (ract-lact) == (i-1-l) && lact > l){
                maxSum = sum;
                lact = l;
                ract = i-1;
            }
            l = i+1;
            sum = 0;
        }
        else
            sum += A[i];
    }

    vector<int> res;
    for( ; lact <= ract; lact++)
        res.push_back(A[lact]);
    return res;
}

