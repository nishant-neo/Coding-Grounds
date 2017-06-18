int Solution::evalRPN(vector<string> &A) {
    int n = A.size();
    stack <int> st;
    for( int i = 0; i < n; i++){
        if( A[i] == "+" ||  A[i] == "-" ||  A[i] == "*" ||  A[i] == "/" ){
            int op2 = st.top(); st.pop();
            int op1 = st.top(); st.pop();
            if( A[i] == "+")
                st.push( op1 + op2 );
            else if( A[i] == "-")
                st.push( op1 - op2 );
            else if( A[i] == "*")
                st.push( op1 * op2 );
            else if( A[i] == "/")
                st.push( op1 / op2);
        }
        else{
            st.push(stoi(A[i]));
        }
    }
    return st.top();
}
