#define MAX(a,b) a > b ? a : b
#define MIN(a,b) a < b ? a : b
vector<Interval> Solution::insert(vector<Interval> &intervals, Interval newInterval) {
    newInterval.start = MIN(newInterval.start, newInterval.end);
    newInterval.end = MAX(newInterval.start, newInterval.end);
    int n = intervals.size();
    vector <Interval>res;
    int i = 0;
    while(i < n && intervals[i].end < newInterval.start){
        res.push_back(intervals[i]);
        i++;
    }
    while( i < n && intervals[i].start <= newInterval.end){
        newInterval.start = MIN(newInterval.start, intervals[i].start);
        newInterval.end = MAX(newInterval.end, intervals[i].end);
        i++;
    }
    res.push_back(newInterval);
    while( i < n){
        res.push_back(intervals[i]);
        i++;
    }
    return res;

}
