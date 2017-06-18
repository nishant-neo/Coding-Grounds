vector <int> st;
vector <int> minst;
MinStack::MinStack() {
    st.clear();
    minst.clear();
}

void MinStack::push(int x) {
    if( minst.size() == 0 || minst[minst.size()-1] >= x)
        minst.push_back(x);
    st.push_back(x);
}

void MinStack::pop() {
    if( st.size() == 0)
        return;
    if( minst[minst.size()-1] == st[st.size()-1] )
        minst.erase(minst.end()-1);
    st.erase(st.end()-1);
}

int MinStack::top() {
    int length = st.size();
    if( length == 0)
        return -1;
    return st[st.size()-1];
}

int MinStack::getMin() {
    if( st.size() == 0)
        return -1;
    return minst[minst.size()-1];
}


