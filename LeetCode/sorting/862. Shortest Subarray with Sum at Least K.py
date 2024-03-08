"""
862. Shortest Subarray with Sum at Least K
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            if nums[0] == k:
                return 1
            return -1

        # queue of indices of prefix sums 
        queue = collections.deque()

        prefix_sums = [0]
        for num in nums :
            # get the sum value by using value up to here process  
            prefix_sums.append(prefix_sums[-1] + num)

        min_size = n + 1 
        for index, value in enumerate(prefix_sums) :
            while queue and value <= prefix_sums[queue[-1]] : 
                # remove the item most recently queued
                queue.pop() 

            # while you have a queue and the value minus the front value is greater than or equal to k
            while queue and value - prefix_sums[queue[0]] >= k : 
                # set min size to the min of itself and the distance between index and leftmost index of queue 
                min_size = min(min_size, index - queue.popleft())
            # append the index at the end of the loop to the queue 
            queue.append(index)

        return -1 if min_size == n+1 else min_size


      # Solution when the numbers are all positive
      # window_sum = 0
          # min_length = 10**6
          # l, r = 0, 0
          # while l < n and r < n:
          #     window_sum += nums[r]
  
          #     print(window_sum)
          #     if window_sum >= k:
          #         min_length = min(min_length, r-l+1)
  
          #     while window_sum >= k and l < r:
          #         # print("ff", window_sum)
          #         window_sum -= nums[l]
          #         l += 1
  
          #         if window_sum >= k:
          #             min_length = min(min_length, r-l+1)
  
          #     r += 1





        
