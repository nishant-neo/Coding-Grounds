/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
#define MAX(a,b) a>b?a:b;
int myCompFunc( const Interval &a, const Interval & b)
{
    return a.start < b.start;
}
vector<Interval> Solution::merge(vector<Interval> &A) {
    int n = A.size();
    sort( A.begin(), A.end(), myCompFunc);
    vector <Interval> res;
    res.push_back(A[0]);
    for( int i = 1; i < n; i++){
        if( res[res.size()-1].end >= A[i].start){
            res[res.size()-1].end = MAX( res[res.size()-1].end, A[i].end );
        }
        else{
            res.push_back(A[i]);
        }
    }
    return res;
}
