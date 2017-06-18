string Solution::countAndSay(int A) {
    string res = "1";
    for( int i = 1 ; i < A; i++){
        string temp = "";
        for( int j = 0 ; j < res.size(); j++){
            int left = j;
            while( j+1 < res.size() && res[j] == res[j+1])
                j++;
            temp += to_string(j-left+1) + res[j];
        }
        res = temp;
    }
    return res;


}

