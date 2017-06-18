bool isValid(vector <string> &ans, int row, int col ){
    for( int j = 0; j < row; j++){
        if( ans[j][col] == 'Q')
            return 0;
    }
    for( int k = row-1, l = col-1; (k >= 0) && (l >= 0); k--, l-- ){
            if( ans[k][l] == 'Q')
                return 0;
    }
    for( int k = row-1, l = col+1; (k >= 0) && (l < ans.size()); k--, l++ ){
            if( ans[k][l] == 'Q')
                return 0;
    }
    return 1;
}
void printArray( vector <string> &ans){
    for( int i  = 0 ; i < ans.size(); i++)
        cout<<ans[i]<<endl;
}
void solveNQueensHelper( int A, int row, vector<vector<string> > &res, vector <string> ans){
    if( row == A){
        res.push_back(ans);
        return;
    }
    //cout<<"***"<<row<<endl;
    //printArray(ans);
    for( int col = 0; col < A; col++){
        ans[row][col] = 'Q';
        if( isValid( ans, row, col))
            solveNQueensHelper(  A, row+1, res, ans);
        ans[row][col] = '.';
    }
}
vector<vector<string> > Solution::solveNQueens(int A) {
    vector<vector<string> > res;
    vector <string> ans(A);
    string str = "";
    for ( int  t = 0; t < A; t++)
        str += ".";
    for( int col = 0; col < A; col++)
        ans[col] = str;
    solveNQueensHelper( A, 0,  res,  ans);
    return res;

}
