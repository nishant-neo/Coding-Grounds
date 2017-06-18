void paranthesis(vector<string> &s, string ans, int n, int open, int close){
    if(open == close && close == n) {
        s.push_back(ans);
        return;
    }
    if( open > n || close > n)
        return;
    if(open < n) {
       ans.push_back('(');
       paranthesis(s, ans, n, open+1, close);
       ans.pop_back();
    }
    if(open > close) {
        ans.push_back(')');
        paranthesis(s, ans, n, open, close+1);
        ans.push_back('(');
    }

}
vector<string> Solution::generateParenthesis(int A) {
    vector<string> s;
    string temp="";
    paranthesis(s,temp,A,0,0);
    return s;

}
