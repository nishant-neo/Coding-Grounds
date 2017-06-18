struct Node{
    int val;
    int l;
    int r;
};

bool operator<(const Node& l, const Node& r) {
     return (l.val<r.val || (l.val == r.val && l.l < r.l) || (l.val == r.val && l.l == r.l && l.r < r.r) );
}
Node makeNode( int v, int a, int b){
    Node n;
    n.val = v;
    n.l = a;
    n.r = b;
    return n;
}
vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    int n = A.size();
    vector<int> res;
    sort( A.begin(), A.end());
    sort( B.begin(), B.end());
    map <Node, int> pq;
    set<int> myset;
    pq[makeNode(A[n-1]+B[n-1], n-1, n-1)] += 1;
    while( res.size() != n){
        Node t = (pq.rbegin())->first;
        pq[t] -= 1;
        pq.erase(t);
        res.push_back( t.val );
        int r = t.r;
        pq[makeNode(A[l]+B[r-1], l,r-1 )] += 1;
        pq[makeNode(A[l-1]+B[r], l-1,r )] += 1;
    }
    return res;

}

