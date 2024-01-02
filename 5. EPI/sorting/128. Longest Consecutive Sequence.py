"""
128. Longest Consecutive Sequence
Solved
Medium

Topics

Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dic = { num:1 for num in nums}
        visited = set()
        count = 0
        max_count = 0
        for num in nums:
            if num in visited:
                continue
            
            count = 1
            visited.add(num)

            reverse_num = num-1
            while reverse_num in nums_dic:
                count += 1
                visited.add(reverse_num)
                reverse_num = reverse_num-1

            forward_num = num+1
            while forward_num in nums_dic:
                count += 1
                visited.add(forward_num)
                forward_num = forward_num+1

            max_count = max(max_count, count)

        return max_count

        


        
