"""
729. My Calendar I
Solved
Medium

Topics

Companies

Hint
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""

from bisect import bisect, insort
class MyCalendar:

    def __init__(self):
        # self.booked = SortedList()
        self.schedule = []
        

    def book(self, start: int, end: int) -> bool:
        if len(self.schedule) == 0:
            self.schedule.append((start,end))
            return True

        idx_to_be_placed = bisect(self.schedule, (start,end))
        # print(idx_to_be_placed)

        if idx_to_be_placed-1 >= 0:
            to_consider = self.schedule[idx_to_be_placed-1]
            if start < to_consider[1]:
                # print("-1",start,end, self.schedule, to_consider)
                return False
        
        if idx_to_be_placed < len(self.schedule):
            to_consider = self.schedule[idx_to_be_placed]
            if end > to_consider[0]:
                # print("+1",start,end, self.schedule, to_consider)
                return False
        

        insort(self.schedule, (start,end))
        # print(start,end, self.schedule, "can book")
        return True


        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
