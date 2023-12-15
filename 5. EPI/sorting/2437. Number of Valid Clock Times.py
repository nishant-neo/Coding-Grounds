"""
You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

 
"""

class Solution:
    def countTime(self, time: str) -> int:
        pattern = time.replace('?', '.')
        return sum(
            # this is the way to format string when we want to pad extra 0s
            
            re.fullmatch(pattern, f'{hour:02}:{minute:02}') is not None
            for hour in range(24)
            for minute in range(60)
        )

        
        # choices = [3, 10, 1, 6, 10]

        # valid_clock_times = 1
        
        
        # if time[1] != '?':
        #     if int(time[1]) < 4:
        #         for choice, ch in zip(choices, time):
        #             if ch == '?':
        #                 valid_clock_times *= choice
        #     else:
        #         choices = [2, 10, 1, 6, 10]
        #         for choice, ch in zip(choices, time):
        #             if ch == '?':
        #                 valid_clock_times *= choice


        # else:
        #     # print("yes2")
        #     if time[0] == '?':
        #         # print("yes12")
        #         valid_clock_times = 24
        #         for choice, ch in zip(choices[2:], time[2:]):
        #             if ch == '?':
        #                 valid_clock_times *= choice

        #     else:
        #         # print("yes22")
        #         if time[0] in ['0', '1']:
        #             # print("yes221")
        #             valid_clock_times = 10
        #             for choice, ch in zip(choices[2:], time[2:]):
        #                 if ch == '?':
        #                     valid_clock_times *= choice
        #         else:
        #             valid_clock_times = 4
        #             for choice, ch in zip(choices[2:], time[2:]):
        #                 if ch == '?':
        #                     valid_clock_times *= choice


        # return valid_clock_times





        
