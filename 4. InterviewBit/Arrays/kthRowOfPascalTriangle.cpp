vector<int> Solution::getRow(int A) {
    vector <vector <int> > res;
    vector <int> Ar;
    Ar.push_back(1);
    if( A == 0)
        return Ar;
    Ar.push_back(1);
    if( A == 1)
        return Ar;
    for( int i = 2; i <= A; i++)
    {
        vector <int> temp;
        temp.push_back(1);
        for( int j = 1; j < Ar.size(); j++){
            temp.push_back(Ar[j-1]+Ar[j]);
        }
        temp.push_back(1);
        Ar.swap(temp);
    }
    return Ar;
}
