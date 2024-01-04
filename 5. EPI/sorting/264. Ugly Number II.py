"""
264. Ugly Number II
Medium

Topics

Companies

Hint
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        nums = [0]*n
        nums[0] = 1
        a=b=c=0

        for i in range(1, n):
            nums[i] = min(nums[a]*2, nums[b]*3, nums[c]*5)

            if nums[i] == nums[a]*2:
                a+=1
            if nums[i] == nums[b]*3:
                b+=1
            if nums[i] == nums[c]*5:
                c+=1

        print(nums)

        return nums[n-1]

        
