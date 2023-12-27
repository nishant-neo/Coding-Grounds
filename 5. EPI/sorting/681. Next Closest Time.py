"""
681. Next Closest Time
Solved
Medium

Topics

Companies
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
 

Constraints:

time.length == 5
time is a valid time in the form "HH:MM".
0 <= HH < 24
0 <= MM < 60
"""
class Solution:
    def nextClosestTime(self, time: str) -> str:

        time_set = set(time)

        is_valid_hour = {i:True for i in range(24)} 
        is_valid_minute = {i:True for i in range(60)} 
        for hour in range(24):
            hour_str = f'{hour:02}'
            for c in hour_str:
                if c not in time_set:
                    is_valid_hour[hour] = False

        for minute in range(60):
            minute_str = f'{minute:02}'
            for c in minute_str:
                if c not in time_set:
                    is_valid_minute[minute] = False


        hour_int = int(time[0:2])
        minute_int = int(time[3:])

        for minute in range(minute_int+1, 60):
            if is_valid_hour[hour_int] and is_valid_minute[minute] and f'{hour_int:02}:{minute:02}' != time:
                return f'{hour_int:02}:{minute:02}'

        
        for hour in range(hour_int+1,hour_int+24):
            hour = hour % 24
            print(hour)
            for minute in range(0, 60):
                if is_valid_hour[hour] and is_valid_minute[minute] and f'{hour:02}:{minute:02}' != time:
                    return f'{hour:02}:{minute:02}'

        return time


        
