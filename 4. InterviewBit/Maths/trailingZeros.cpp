int Solution::trailingZeroes(int n) {
    if( n < 0 )
        return 0;
    int count = 0;
    int five = 5;
    while( five <= n){
        count += n / five;
        five *= 5;
    }
    return count;
}
