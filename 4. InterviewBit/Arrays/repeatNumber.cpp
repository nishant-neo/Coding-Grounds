int Solution::repeatedNumber(const vector<int> &A) {
    int n = A.size();

    int bin1, bin2, count1 = 0, count2 = 0;
    for( int i = 0; i < n ; i++){
        if( A[i] == bin1 && count1 > 0)
            count1++;
        else if( A[i] == bin2 && count2 > 0)
            count2++;
        else if( count1 == 0){
            bin1 = A[i];
            count1++;
        }
        else if( count2 == 0){
            bin2 = A[i];
            count2++;
        }
        else{
            count1--;
            count2--;
        }
    }
    count1 = 0, count2 = 0;
    for( int i = 0; i < n; i++){
        if( A[i] == bin1)
            count1++;
        if( A[i] == bin2)
            count2++;
    }
    if( count1 > (n / 3) )
        return bin1;
    else if( count2 > ( n/3))
        return bin2;
    else
        return -1;
}
