
int Solution::majorityElement(const vector<int> &A) {
    int n = A.size();
    int bucket, count = 0;

    for( int i = 0; i < n; i++){
        if( count == 0){
            bucket = A[i];
            count++;
        }
        else if( bucket == A[i])
            count++;
        else
            count--;
    }
    return bucket;
}
