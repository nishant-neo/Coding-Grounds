vector<int> Solution::twoSum(const vector<int> &A, int B) {
    vector<int>res;
    int n = A.size();
    if( n == 0)
        return res;
    unordered_map<long long int, int> um;

    long long sum = 0; int min = INT_MAX, max = INT_MAX-1;
    for( int i = 0 ; i < n; i++){
        sum = A[i];
        if( um.find(B -sum) != um.end() ){
            int tmin = um[B -sum];
            int tmax = i;
            if( tmax < max || (tmax == max && tmin < min) ){
                min = tmin;
                max = tmax;
            }
        }
        if( um.find(sum) == um.end() )
            um[sum] = i;
    }
    if( min != INT_MAX ){
        res.push_back(min+1);
        res.push_back(max+1);
    }
    return res;

}
