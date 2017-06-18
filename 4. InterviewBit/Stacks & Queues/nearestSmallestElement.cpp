vector<int> Solution::prevSmaller(vector<int> &A) {
    int n = A.size();
    vector <int> NSE;

    stack <int> st;
    st.push( -1);
    for( int i = 0; i < n; i++){
        int next = A[i];
        if( next > st.top() )
        {
            NSE.push_back(st.top());
            st.push(next);
        }
        else{

            while( next <= st.top())
                st.pop();
            NSE.push_back(st.top());
            st.push(next);
        }
    }
    return NSE;

}

