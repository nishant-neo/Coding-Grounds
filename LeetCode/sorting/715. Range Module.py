"""
715. Range Module
Solved
Hard
Topics
Companies
Hint
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
 

Constraints:

1 <= left < right <= 109
At most 104 calls will be made to addRange, queryRange, and removeRange.
"""

class RangeModule:

    def __init__(self):
        self.intervals = []

    def touching_ranges(self, left, right):
        '''find all the ranges that touch interval [left, right]'''
        i, j = 0, len(self.intervals)-1
        step = len(self.intervals) // 2
        while step >= 1:
            while i + step < len(self.intervals) and self.intervals[i+step-1][1] < left:
                i += step
            while j - step >= 0 and self.intervals[j-step+1][0] > right:
                j -= step
            step //= 2
        return i, j
        
    def addRange(self, start: int, end: int) -> None:
        if len(self.intervals) == 0 or self.intervals[-1][1] < start:
            self.intervals.append((start, end))
            return

        if self.intervals[0][0] > end:
            self.intervals = [(start, end)] + self.intervals
            return

        i, j = self.touching_ranges(start, end)
        self.intervals[i:j+1] = [(min(self.intervals[i][0], start), max(self.intervals[j][1], end))]



    def queryRange(self, left: int, right: int) -> bool:
        if len(self.intervals) == 0: 
            return False
        i, j = self.touching_ranges(left, right)
        return self.intervals[i][0] <= left and right <= self.intervals[i][1]
                

    def removeRange(self, left: int, right: int) -> None:
        if not self.intervals or self.intervals[0][0] > right or self.intervals[-1][1] < left: 
            return
        i, j = self.touching_ranges(left, right)
        new_ranges = []
        for k in range(i, j+1):
            if self.intervals[k][0] < left:
                new_ranges.append((self.intervals[k][0], left))
            if self.intervals[k][1] > right:
                new_ranges.append((right, self.intervals[k][1]))
        self.intervals[i:j+1] = new_ranges
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
