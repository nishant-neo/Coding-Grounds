"""
1353. Maximum Number of Events That Can Be Attended
Solved
Medium
Topics
Companies
Hint
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
"""

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        start, end = float("inf"), float("-inf")
        
        for i,j in events:
            start = min(start,i)
            end = max(end,j)


        c, i, h = 0, 0 , []

        for day in range(start, end+1):
            while i < n and events[i][0]== day:
                heapq.heappush(h, events[i][1])
                i += 1

            while h and h[0] < day:
                heapq.heappop(h)

            if h:
                heapq.heappop(h)
                c += 1

        return c

        # DIFFICULT TO UNDESSTAND


        events.sort()

        # only for no duplication `while` after `for`
        events.append([float('inf'), float('inf')])

        result = 0
        h = []
        current_day = 0

        for start, end in events:
            while h and current_day < start:
                prev_end = heapq.heappop(h)
                if prev_end >= current_day:
                    result += 1
                    current_day += 1
            
            current_day = start
            heapq.heappush(h, end)
        
        return result



        
        
        # return 0


        
