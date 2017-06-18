vector<string> Solution::fizzBuzz(int A) {
    vector <string> res(A);
    if( A == 0)
        return res;

    for( int i = 0; i < A; i++)
        res[i] = to_string(i+1);

    for (int i = 2; i < A; i = i+3)
        res[i] = "Fizz";

    for( int i = 4; i < A; i = i+5){
        if( res[i] == "Fizz")
            res[i] += "Buzz";
        else
            res[i] = "Buzz";
    }
    return res;

}

