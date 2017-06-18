int Solution::bulbs(vector<int> &A) {
    int n = A.size();
    int inv = 0, count = 0;
    for( int i = 0; i < n; i++){
        if( (A[i] + inv)%2  == 0){
            count++;
            if( inv == 0)
                inv = 1;
            else
                inv = 0;
        }
    }
    return count;

}

