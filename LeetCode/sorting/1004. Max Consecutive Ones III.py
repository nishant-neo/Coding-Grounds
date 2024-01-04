"""
1004. Max Consecutive Ones III
Solved
Medium

Topics

Companies

Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        used_k = 0
        max_consecutive_ones = 0

        l, r = 0, 0
        while(l<=r and r<len(nums)):
            if nums[r] == 0:
                used_k += 1
                while(used_k > k):
                    if nums[l] == 0:
                        used_k -= 1
                    l += 1
            r += 1
            max_consecutive_ones = max(max_consecutive_ones, (r-l))

        return max_consecutive_ones


        
            

            

        
