string Solution::convertToTitle(int A) {
    if( A == 0)
        return "";
    string res = "";
    while( A  ){
        if( A % 26 == 0){
            res += 'Z';
            A -= 26;
        }
        else{
            char ch = A%26 + 'A' - 1;
            res += ch;
        }
        A = A / 26;
    }
    reverse( res.begin(), res.end());
    return res;
}
