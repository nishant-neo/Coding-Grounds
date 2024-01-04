"""
896. Monotonic Array
Solved
Easy

Topics

Companies
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        last = nums[0]
        inc_flag = False
        dec_flag = False
        for num in nums[1:]:
            if num > last:
                inc_flag = True
            if num < last:
                dec_flag = True
            last = num
            if inc_flag and dec_flag:
                return False

        return True


        
