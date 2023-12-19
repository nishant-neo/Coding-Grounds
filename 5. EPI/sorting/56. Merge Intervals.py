"""
56. Merge Intervals
Solved
Medium

Topics

Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        
        res_ptr = 0
        intervals_ptr = 1

        while(intervals_ptr<len(intervals)):
            res_interval = res[res_ptr]
            curr_interval = intervals[intervals_ptr]
            
            if curr_interval[0] <= res_interval[1]:
                res[res_ptr][1] = max(curr_interval[1],res[res_ptr][1])
            else:
                res.append(curr_interval)
                res_ptr += 1


            intervals_ptr += 1

        return res
