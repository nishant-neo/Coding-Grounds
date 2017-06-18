int maxVal( int a, int b, int c){
    return a > max( b, c) ? a : max(b,c);
}
int Solution::maxp3(vector<int> &A) {
    int n = A.size();
    if(n == 3)
        return A[0]*A[1]*A[2];
    /*
    int maxel = A[0] >= A[1] ? A[0] : A[1];
    int secondMax = A[0] < A[1] ? A[0] : A[1];

    for( int i = 2; i < n; i++){
        if( A[i] > max){
            secondMax = max;
            max = A[i];
        }
        else if( A[i] > secondMax)
            secondMax = A[i];
    }*/
    sort( A.begin(), A.end());

    return A[0]*A[1]*A[n-1] > A[n-1]*A[n-2]*A[n-3] ? A[0]*A[1]*A[n-1] : A[n-1]*A[n-2]*A[n-3] ;
}

