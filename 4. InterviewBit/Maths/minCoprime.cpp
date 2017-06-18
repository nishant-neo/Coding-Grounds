int gcd(int A, int B)
{
    if( B != 0)
        return gcd( B, A%B);
    else
        return A;
}
int Solution::cpFact(int A, int B) {
    int t = B;
    if( gcd(A,B) == 1)
        return A;
    int i = 2;
    while( gcd(A,B) != 1)
    {
        if( A % i == 0 && B % i == 0)
        {
            while( A%i == 0)
                A = A/i;
            while( B%i == 0)
                B = B/i;

        }
        i++;
    }
    return A;


}
