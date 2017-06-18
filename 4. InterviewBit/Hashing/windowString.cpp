#define MIN(a,b) a < b ? a : b

bool check( unordered_map <char, int> &Tstring){
    for( unordered_map <char, int>:: iterator it = Tstring.begin(); it != Tstring.end(); ++it){
        if( it -> second > 0)
            return 0;
    }
    return 1;
}
string Solution::minWindow(string S, string T) {
    unordered_map <char, int> Tstring;

    for( int i = 0; i < T.size(); i++)
        Tstring[T[i]]++;
    int s = 0, min = INT_MAX, min_s = INT_MAX, min_i = INT_MAX, fla = 0;
    for( int i = 0; i < S.size(); i++){
        if( Tstring.find( S[i]) != Tstring.end())
            Tstring[S[i]]--;
        if( check(Tstring)  ){
                while (Tstring.find(S[s]) == Tstring.end() || Tstring[S[s]] < 0) {
                    if (Tstring.find(S[s]) != Tstring.end()) Tstring[S[s]]++;
                    s++;
                }
            if( min > (i-s+1)){
                min = i-s+1;
                min_s = s;
                min_i = i;
            }
        }
    }
    if( min_s == INT_MAX)
        return "";
    return S.substr(min_s, min);
}
