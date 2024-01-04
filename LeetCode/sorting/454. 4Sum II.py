"""
454. 4Sum II
Solved
Medium

Topics

Companies
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        nums3.sort()
        nums4.sort()

        def get_sums(nums1, nums2):
            sum_dic = {}
            for num1 in nums1:
                for num2 in nums2:
                    sum_dic[(num1+num2)] = sum_dic.get(num1+num2,0)+1

            return sum_dic

        sum_dic1 = get_sums(nums1, nums2)
        sum_dic2 = get_sums(nums3, nums4)

        # print(sum_dic1)
        # print(sum_dic2)

        res = 0
        for k1,v1 in sum_dic1.items():
            for k2,v2 in sum_dic2.items():
                if (k1+k2 == 0):
                    res += (v1*v2)

        return res
