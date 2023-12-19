"""
949. Largest Time for Given Digits
Solved
Medium

Topics

Companies
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
 

Constraints:

arr.length == 4
0 <= arr[i] <= 9
"""

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        s = f"{arr[0]}{arr[1]}:{arr[2]}{arr[3]}"

        prospect_result = [[]]
        result = sorted(arr)
        
        def get_permutation(i):
            if i == len(result):
                return
            if (result[0]*10+result[1]) in range(0,24) and (result[2]*10+result[3]) in range(0,60):
                prospect_result.append(result.copy())
            for j in range(i, len(result)):
                result[i], result[j] = result[j], result[i]
                get_permutation(i+1)
                result[i], result[j] = result[j], result[i]
            return

        # 
        get_permutation(0)
        prospect_result = sorted(prospect_result)

        return "" if len(prospect_result[-1]) == 0 else f"{prospect_result[-1][0]}{prospect_result[-1][1]}:{prospect_result[-1][2]}{prospect_result[-1][3]}"


