vector<int> Solution::lszero(vector<int> &A) {
    vector <int> res;
    int n = A.size();
    if( n == 0)
        return res;
    long long int sum = 0, max = -2 , min = -1, zmin, zmax ;
    unordered_map <long long int,int> um;
    um[0] = -1;
    for( int i = 0; i < n; i++){
        sum += A[i];
        if( um.find(sum) == um.end() )
            um[sum] = i;
        else{
            int tmin, tmax;
            tmin = um[sum];
            tmax = i;
            if( (tmax - tmin) > (max-min) || ((tmax - tmin) == (max-min) && tmin < min) ){
                min = tmin;
                max = tmax;
            }
        }
    }
    for( int i = min+1 ; i <= max; i++)
        res.push_back(A[i]);
    return res;
}

