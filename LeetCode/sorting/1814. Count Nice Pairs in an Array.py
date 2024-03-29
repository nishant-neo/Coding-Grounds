"""
1814. Count Nice Pairs in an Array
Solved
Medium
Topics
Companies
Hint
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

"""

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 1000000007
        # here the property is if nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        # by rearrangement nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # we just count the occurences and find the pairs
        dif_rev_nums = [ int(str(num)[::-1])-num for num in nums]
        
        # count_diffs = Counter(dif_rev_nums)
        # res = 0
        # for k, v in count_diffs.items():
        #     if v == 2:
        #         res = (res + 1) % MOD
        #     elif v > 2:
        #         res = (res + (v * (v-1))//2) % MOD
        
        # Another way of doing permutations
        res = 0
        count_diffs = defaultdict(int)
        for num in dif_rev_nums:
            res = (res + count_diffs[num]) % MOD
            count_diffs[num] += 1


        return res
        
