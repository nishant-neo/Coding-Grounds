bool myComparator( string x, string y){
    return x+y > y+x;
}
string Solution::largestNumber(const vector<int> &A) {
    vector <string> str;
    for( int i = 0 ; i < A.size() ; i++)
        str.push_back(to_string(A[i]));
    sort( str.begin(), str.end(), myComparator);
    string res = "";
    for( int i = 0 ; i < A.size(); i++){
       // cout<<str[i]<<" ";
        res += str[i];
    }
    int pos = 0;
    while( pos < A.size()-1 && res[pos] == '0')
        pos++;
    return res.substr(pos, res.size()-pos+2);
}
