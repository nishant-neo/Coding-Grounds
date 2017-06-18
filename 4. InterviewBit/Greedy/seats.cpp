int Solution::seats(string A) {
    int i,n=A.length(),x=0,l=0,med;
    long long int res = 0;
    for(i=0;i<n;i++){
        if(A[i]=='x')
            x++;
    }
    if( x == 0)
        return 0;
    for(i=0;i<n;i++){
        if(A[i]=='x'){
            l++;
            if(l==(x/2)+1){
                med=i;
                break;
            }
        }
    }


    //left
    int r = med;

    for( int i = 0; i < r; i++ ){
        while( A[r] == 'x')
            r--;
        if( i < r && A[i] == 'x' ){
            A[i] = '.';
            A[r] = 'x';
            res += ( r -i );
            r--;
        }


    }
    //cout<<res<<endl;

    //right
     l = med;
    while( A[l] == 'x')
            l++;

    for( int i = n-1; i > l; i-- ){
        while( A[l] == 'x')
            l++;
        if( i > l && A[i] == 'x' ){
            A[i] = '.';
            A[l] = 'x';
            res += ( i -l  );
            l++;
        }


    }
    return res%10000003;
}

