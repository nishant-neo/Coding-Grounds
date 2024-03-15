"""
493. Reverse Pairs
Solved
Hard
Topics
Companies
Hint
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

Constraints:

1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""

from sortedcontainers import SortedList

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         sl = SortedList(num * 2 for num in nums)

#         result = 0
#         for num in nums:
#             sl.remove(num * 2)
#             result += sl.bisect_left(num)
#         return result

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         ans = 0
#         seen = []
#         for x in nums: 
#             k = bisect_right(seen, 2*x)
#             ans += len(seen) - k
#             insort(seen, x)
#         return ans 

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         countit = 0
#         for j in range(n):
#             for i in range(0, j):
#                 if nums[i] > 2*nums[j]:
#                     countit += 1

#         return countit


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # def sortit(l1,l2):
        #     result = []
        #     l1 = deque(l1)
        #     l2 = deque(l2)
        #     while l1 and l2:
        #         if l1[0] <= l2[0]:
        #             result.append(l1.popleft())
        #         else:
        #             result.append(l2.popleft())
        #     result.extend(l1 or l2)
        #     return result

        def merge_sort(start, end):
            if start >= end:
                return 0
            
            mid = start + (end-start)//2
            count = merge_sort(start, mid) + merge_sort(mid+1, end)

            i = start
            j = mid + 1
            while i <= mid and j <= end:
                if nums[i] > 2*nums[j]:
                    count += mid-i+1
                    j += 1
                else:
                    i += 1

            nums[start:end+1] = sorted(nums[start:end+1])

            return count

        return merge_sort(0, len(nums) - 1)

        
