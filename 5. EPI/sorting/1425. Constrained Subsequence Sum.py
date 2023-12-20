"""
1425. Constrained Subsequence Sum
Solved
Hard

Topics

Companies

Hint
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):

            # here since we need the maximum element so even
            # if the elements beyond k are present, but they are
            # not amongst the max, we dont care about them, and if 
            # max element is beyond k, will pop it out 
            while i-heap[0][1] > k:
                heapq.heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr,i))

        return ans
        # n = len(nums)

        # dp = [0]*(n)
        # top

        # for i,num in enumerate(nums):
        #     max_num = 0
        #     for j in range(k):
        #         if (i-j-1) >= 0:
        #             # here we are gettin TLE with linear time
        #             max_num = max(max_num, dp[i-j-1])

        #     dp[i] = num + max_num

        #     # print(f"dp[i]={dp[i]} num={num}")

                

        # return max(dp)
