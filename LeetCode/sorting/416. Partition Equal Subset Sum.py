"""
416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        to_find = int(sum_nums / 2)

        # top down approach
        @lru_cache(maxsize=None)
        def dfs(n, sum_to_find):
            if sum_to_find == 0:
                return True
            if n == 0 or sum_to_find < 0:
                return False

            return dfs(n-1, sum_to_find) or dfs(n-1, sum_to_find-nums[n]) 

        return dfs(len(nums)-1, to_find)

        # bootom up approach
        # dp = [False for _ in range(to_find+1)]
        # dp[0] = True

        # for num in nums:
        #     for i in reversed(range(num, len(dp))):
        #         if (i-num >= 0):
        #             dp[i] = dp[i] or dp[i-num]

        # return dp[-1]

        

                

        
