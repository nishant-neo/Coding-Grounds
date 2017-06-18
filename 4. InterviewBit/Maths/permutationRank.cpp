#define M 1000003
int fact( int n ){
    if( n == 0)
        return 1;
    return ((n % M) * fact(n-1)%M)%M;
}
int smallerThanCur( string &A, int in){
    int count = 0;
    for( int i = in; i < A.size(); i++)
        if( A[i] < A[in])
            count++;
    return count;
}
int Solution::findRank(string A) {
    int n = A.size();

    long long int x = 0;
    for( int i = 0 ; i < n; i++){
        int r = smallerThanCur( A, i);
        x = x + (fact(n - i -1) * r%M)%M;
        x = x % M;
    }

    return x+1;
}
