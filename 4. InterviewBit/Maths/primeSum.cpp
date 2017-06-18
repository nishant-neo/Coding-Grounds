bool isPrime(int n){
    for(int i = 2; i*i <= n; ++i)
    {
        if( n%i == 0)
            return false;
    }
    return true;
}
vector<int> Solution::primesum(int A) {
    int i;
    for( i = 2; i <= A; i++)
    {
        if( isPrime(i) && isPrime(A-i))
            break;
    }
    vector <int> res;
    res.push_back(i);
    res.push_back(A-i);
    return res;
}

