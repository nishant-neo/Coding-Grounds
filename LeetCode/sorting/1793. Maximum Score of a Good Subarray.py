"""
1793. Maximum Score of a Good Subarray
Solved
Hard
Topics
Companies
Hint
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        neighbours = []

        l, r = k, k
        max_res = nums[k]
        min_el = nums[k]
        while l >= 0 or r < n:
            # print(l, r)
            if r+1 < n and l-1 >= 0:
                if nums[r+1] > nums[l-1]:
                    r += 1
                    min_el = min(min_el, nums[r])
                else:
                    l -= 1
                    min_el = min(min_el, nums[l])
            elif r+1 < n:
                r += 1
                min_el = min(min_el, nums[r])
            elif l-1 >= 0:
                l -= 1
                min_el = min(min_el, nums[l])
            else:
                break

            max_res = max(max_res, min_el*(r-l+1))

        return max_res
        
