"""
1218. Longest Arithmetic Subsequence of Given Difference
Solved
Medium

Topics

Companies

Hint
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
 

Constraints:

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        # n = len(arr)
        # lis = [1]*n

        # for idx,num in enumerate(arr):
        #     max_j = 0
        #     for j in range(idx):
        #         if (num-arr[j] == difference):
        #             max_j = max(max_j, lis[j])
        #     lis[idx] = 1+max_j
        #     # print(lis)
        # return max(lis)

        n = len(arr)
        lis = [1]*n
        max_subsequence = 1
        cache = {}
        
        for idx,num in enumerate(arr):
            max_len = 1
            if num-difference in cache:
                max_len = cache[num-difference]+1
            cache[num] = max(cache.get(num,1), max_len)
            max_subsequence = max(max_subsequence, max_len)

        # print(cache)

        return max_subsequence
