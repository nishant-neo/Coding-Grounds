"""
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        # if we think about it the 3 elements that will impact is last 3 elements from last
        # or the bgining, so we use this
        # Here, at most 8 numbers are relevant, i.e. the 4 smallest and the 4 largest. Suppose they are labeled as
        # m1, m2, m3, m4, ... M4, M3, M2, M1
        # then min(M4-m1, M3-m2, M2-m3, M1-m4) gives the solution. It is linear O(N) to find m1-m4 and M1-M4 like below.
        # O(N) time & O(1) space leveraging on the heapq module
        n = len(nums)
        if n < 4:
            return 0
        nums.sort()

        possible_index = [0, 1, 2, n-1, n-2, n-3]

        min_diff = nums[n-1]-nums[0]
        for i in range(6):
            _i = possible_index[i]
            for j in range(i+1,6):
                _j = possible_index[j]
                for k in range(j+1,6):
                    _k = possible_index[k]

                    remove_set = set([_i, _j, _k])
                    min_left_index = min(set([0, 1, 2, 3]) - remove_set) 
                    max_right_index = max(set([n-1, n-2, n-3, n-4]) - remove_set) 

                    
                    val = nums[max_right_index]-nums[min_left_index]

                    # print(f"i={_i} j={_j} k={_k} min_left_index={min_left_index} max_right_index={max_right_index} val ={val}")

                    min_diff = min(min_diff, val)


                    
        return min_diff


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0

        nums.sort()

        # here these are the only possibility
        return min(
            (nums[-1] - nums[3]),
            (nums[-2] - nums[2]),
            (nums[-3] - nums[1]),
            (nums[-4] - nums[0])
            )
        
