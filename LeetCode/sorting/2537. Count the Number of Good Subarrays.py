"""
2537. Count the Number of Good Subarrays
Solved
Medium
Topics
Companies
Hint
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109
"""

class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        N, count = len(A), defaultdict(int)
        L =  result = pair_count = 0

        # print(count)
        for i, v in enumerate(A):
            # print(count[v])
            pair_count += count[v] # counting the # pairs
            count[v] += 1
            while L < i and pair_count >= k:
                result += N - i
                count[A[L]] -= 1
                pair_count -= count[A[L]]
                L += 1
        return result
