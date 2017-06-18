vector<int> Solution::repeatedNumber(const vector<int> &A) {
    int n = A.size();

    long long int S = 0, SS = 0;

    long long int sum = 0, squares = 0;
    for( int i = 0; i < n; i++){
        sum += A[i];
        squares += A[i]*A[i];
        sum -= (i+1);
        squares -= (i+1)*(i+1);
    }

    vector<int> res;
    res.push_back( (sum / (2.0*squares)) + (squares / 2.0) );
    res.push_back( (sum / (2.0*squares)) - (squares / 2.0) );
    return res;
}
