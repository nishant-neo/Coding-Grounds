"""
1630. Arithmetic Subarrays
Solved
Medium

Topics

Companies

Hint
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

 

Example 1:

Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
Example 2:

Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]
 

Constraints:

n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-105 <= nums[i] <= 105
"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        # sorted_nums = sorted([(num,idx) for idx,num in enumerate(nums)])

        # ap = [0] * n
        # ap[0] = (-1, -1)
        # ap[1] = (-1, -1)

        # for i in range(2,n):
        #     idx = sorted_nums[i][1]
        #     if (sorted_nums[i][0]-sorted_nums[i-1][0]) == (sorted_nums[i-1][0]-sorted_nums[i-2][0]):
        #         ap[idx] = (sorted_nums[i-2][1],sorted_nums[i-1][1])
        #     else:
        #         ap[idx] = (-1,-1)

        def check(prospect):
            prospect.sort()
            result = True
            # print(prospect)
            for i in range(2,len(prospect)):
                if (prospect[i]-prospect[i-1]) != (prospect[i-1]-prospect[i-2]):
                    result = False
            return result

        def check(arr):
            min_element = min(arr)
            max_element = max(arr)

            if (max_element - min_element) % (len(arr) - 1) != 0:
                return False

            diff = (max_element - min_element) / (len(arr) - 1)
            
            arr_set = set(arr)
            curr = min_element + diff
            while curr < max_element:
                if curr not in arr_set:
                    return False
                
                curr += diff
            
            return True

        
        results = []
        for ll,rr in zip(l,r):
            prospect = []
            for k in range(ll,rr+1):
                prospect.append(nums[k])            
            results.append(check(prospect))

        return results
                    


            



            


        
