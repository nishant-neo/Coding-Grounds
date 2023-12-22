"""
413. Arithmetic Slices
Solved
Medium

Topics

Companies
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        # diff = [0]*n

        last_diff = nums[1]-nums[0]
        last_diff_index = 0
        was_there_an_ap = False
        total_substrings = 0

        for i in range(2,n):
            if nums[i]-nums[i-1] == last_diff:
                # print(i)
                was_there_an_ap = True

            else:
                if was_there_an_ap:
                    length_of_ap = i-last_diff_index
                    count_n = length_of_ap-2
                    total_substrings += int((count_n)*(count_n+1))/2
                    was_there_an_ap = False
                last_diff = nums[i]-nums[i-1]
                last_diff_index = i-1

        if was_there_an_ap:
            length_of_ap = i+1-last_diff_index
            count_n = length_of_ap-2
            # print(length_of_ap, count_n)
            total_substrings += int((count_n)*(count_n+1))/2
            was_there_an_ap = False

        return int(total_substrings)



        
