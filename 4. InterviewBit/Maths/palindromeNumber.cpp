bool Solution::isPalindrome(int A) {
    if( A < 0)
        return 0;
    if( A / 10 == 0)
        return 1;
    long long int x = A, y = 0;
    while( x  ){
        y = y*10 + x%10;
        x = x / 10;
    }
    return ( A == y);
}
