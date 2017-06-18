
int Solution::isValidSudoku(const vector<string> &A) {
    int n = A.size();

    unordered_map <char, int> um;
    //rows
    for( int i = 0 ; i < n; i++ ){
        for( int j = 0; j < n; j++){
            if(A[i][j]!='.'){
                if( um.find(A[i][j]) != um.end())
                    return 0;
                um[A[i][j]] = 1;
            }
        }
        um.clear();
    }
    um.clear();
    //columns
    for( int i = 0 ; i < n; i++ ){
        for( int j = 0; j < n; j++){
            if(A[j][i]!='.'){
                if( um.find(A[j][i]) != um.end())
                    return 0;
                um[A[j][i]] = 1;
            }
        }
        um.clear();
    }
    um.clear();
    //cells
    int a = 0, b = 0;
    for( int i = 2; i < 9; i = i + 3){
        for( int j = 2; j < 9; j = j + 3){
            for(a = i - 2;  a <= i; a++){
                for(b = j - 2; b <= j; b++){
                    if(A[a][b]!='.'){
                        if( um.find(A[a][b]) != um.end())
                            return 0;
                        um[A[a][b]] = 1;
                    }
                }
            }
            um.clear();
        }
    }
    return 1;
}
