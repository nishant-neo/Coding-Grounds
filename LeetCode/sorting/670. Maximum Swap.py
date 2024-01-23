"""
670. Maximum Swap
Solved
Medium
Topics
Companies
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_ = num
        num_list = []
        # num_set
        while(num>0):
            # print(num)
            num_list.append(num%10)
            num = num//10
        num_list = num_list[::-1]
        # num_set = set(num_list)

        # minsofar = []
        maxsofar = [(-1, float(-inf))]*len(num_list)
        prospects = []
        result = 0
        max_result = -1
        for i in reversed(range(0, len(num_list)-1)):
            maxsofar[i] = maxsofar[i+1]
            if num_list[i+1] > maxsofar[i+1][1]:
                maxsofar[i] = (i+1, num_list[i+1])
                
        for i in range(0, len(num_list)):
            idx, val = maxsofar[i]
            if idx == -1:
                return num_
            if val > num_list[i]:
                num_list[idx], num_list[i] = num_list[i], num_list[idx]
                for num in num_list:
                    result = result*10 + num
                return result

