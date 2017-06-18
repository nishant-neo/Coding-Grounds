vector<int> Solution::flip(string A) {
    int n = A.size();

    int l = 0, r = 0, lact = 0, ract = 0;
    long long sum = 0, maxSum = 0, flag =0;
    for( int i = 0; i < n; i++){
        if( A[i] == '1')
            sum--;
        else if( A[i] == '0'){
            sum++;
            flag = 1;
        }
        //cout<<i<<" "<<sum<<" "<<maxSum<<" "<<l<<" "<<l<<endl;
        if( sum > maxSum ){//|| ( (sum == maxSum) && (ract-lact) > (i - l)) ){
            maxSum= sum;
            lact = l+1;
            ract = i+1;
        }
        if( sum < 0){
            sum = 0;
            l = i+1;
        }
    }
    //cout<<lact<<" "<<r<<endl;
    vector <int> res;
    if( !flag )
        return res;
    res.push_back(lact);
    res.push_back(ract);
    return res;

}
