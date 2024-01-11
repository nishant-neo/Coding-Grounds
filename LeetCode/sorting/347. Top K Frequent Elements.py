"""
347. Top K Frequent Elements
Solved
Medium

Topics

Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_histogram = Counter(nums)

        num_histogram_values = [ (-v,k) for k,v in num_histogram.items()]

        heapq.heapify(num_histogram_values)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(num_histogram_values)[1])

        return result
