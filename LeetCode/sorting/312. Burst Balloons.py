"""
312. Burst Balloons
Solved
Hard
Topics
Companies
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""


# top-down apprach
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]


        # Tip: Thinking Backward, instead of thinking of which one to burst first, 
        # we think of which one to burst last. as the thinking forward doesnt make 
        # the two subproblem independent
        # i.e., dp(left, i - 1) and dp(i + 1, right) are not independent, 
        # and cannot be calculated separately
        @cache
        def dp(left, right):
            if right - left < 0:
                return 0

            result = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                remaining = dp(left, i - 1) + dp(i + 1, right)
                # update the result
                result = max(result, remaining + gain)
            return result

    
        return dp(1, len(nums)-2)

# bottoms up approach
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)
        # dp[i][j] is the max number of coins in nums[i:j] range
        dp = [[0 for _ in range(n)] for _ in range(n)] 
        
        for offset in range(2, n):
            for i in range(n - offset):
                j = i + offset
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], balloons[i] * balloons[k] * balloons[j] + \
                                                                    dp[i][k] + dp[k][j])

        return dp[0][n - 1]
        
