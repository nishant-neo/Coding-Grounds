int Solution::colorful(int A) {
    vector <int> num;
    unordered_map <int, int> um;
    while( A){
        if( A % 10 == 0)
            return 0;
        num.push_back( A%10);
        A = A / 10;
    }
    int n = num.size(), prod = 1, prod2 = 1;
    for( int i = 1; i <= n; i++){
        prod *= num[i-1];
        if (um.find(prod) != um.end())  //  means that K does not exist in A.
            return 0;
        um[prod]=1;
        prod2 = prod;
        for( int j  = i; j < n; j++ ){
            prod2 = prod2 / num[j-i];
            prod2 = prod2 * num[j];
            if (um.find(prod2) != um.end())  //  means that K does not exist in A.
                return 0;
            um[prod2]=1;
            }
    }
    return 1;
}

