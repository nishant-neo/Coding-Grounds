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
        n = len(nums)
        
        max_constraint_sum = nums[0]
        queue = deque()
        dp = [0] * len(nums)

        for i in range(n):
            # removing if out of the window size
            if queue and i-queue[0]>k:
                queue.popleft()
            
            # getting the maximum of the sliding window
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            
            # adding to the deque
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            if dp[i] > 0:
                queue.append(i)

            # getting the maximum subsequence sum
            max_constraint_sum = max(max_constraint_sum, dp[i])

        return max_constraint_sum
    
    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
        
    #     max_constraint_sum = nums[0]
    #     heap = [(-nums[0], 0)]

    #     for idx in range(1, n):
    #         num = nums[idx]

    #         while idx-heap[0][1] > k:
    #             heapq.heappop(heap)

    #         curr =  max(0, -heap[0][0]) + num
    #         max_constraint_sum = max(max_constraint_sum, curr)
    #         heapq.heappush(heap, (-curr,idx))

    #     return max_constraint_sum
        

            


        
        

            


        
