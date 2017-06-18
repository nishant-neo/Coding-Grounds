int Solution::reverse(int A) {
    int sign = A < 0 ? -1 : 1;
    A = abs(A);
    if( A < 10)
        return sign*A;
    long long int rev = 0;
    while( A ){
        rev = rev*10 + A%10;
        A = A / 10;
        if( rev < 0)
            return 0;
    }
    if( sign == -1 && rev*sign < INT_MIN || sign == 1 && rev > INT_MAX)
        return 0;
    return sign*rev;
}
