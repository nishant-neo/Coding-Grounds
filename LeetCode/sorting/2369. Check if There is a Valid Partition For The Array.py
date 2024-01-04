"""
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
"""

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums) 
        if n == 1: 
            return False 
        dp = [True, False, nums[0] == nums[1] if n > 1 else False] 
        for i in range(2, n): 
            current_dp = (nums[i] == nums[i-1] and dp[1]) or \
                         (nums[i] == nums[i-1] == nums[i-2] and dp[0]) or \
                         (nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[0])
            dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp 
        return dp[2]
        # nums.sort()

        # __________________________________________________________________
        # RECCURRENCE SOLUTION
        # # @cache
        # def isvalid(arr):
        #     if len(arr) == 2 and arr[0] == arr[1]:
        #         return 1
        #     elif (len(arr) == 3 and (arr[0] == arr[1] and arr[1] == arr[2])):
        #         return 2
        #     elif (len(arr) == 3 and (arr[0]+1 == arr[1] and arr[1]+1 == arr[2])):
        #         return 3
        #     return 0
        

        # # def dfs(arr):
        # #     if len(arr) == 0:
        # #         return True

        # #     if len(arr) == 1:
        # #         return False
        # #     return (isvalid(arr[0:2]) and dfs(arr[2:])) or (isvalid(arr[0:3]) and dfs(arr[3:]))

        # # return dfs(nums)


        # __________________________________________________________________

        # n = len(nums)
        # if n == 2:
        #     return (isvalid(nums[0:2])> 0)
        
        # validarray = [False]*(n+1)
        # validarray[0] = True
        # validarray[2] = (isvalid(nums[0:2])> 0)
        # validarray[3] = (isvalid(nums[0:3])> 0) 

        # isvalidcache = [0]*(n+1)
        # isvalidcache[0] = 1
        # isvalidcache[2] = isvalid(nums[0:2])
        # isvalidcache[3] = isvalid(nums[0:3])

        # for i in range(3, n):
        #     # print(i, nums[i])
        #     # i = t-1

        #     isvalidcache[i+1] = 0
        #     validarray[i+1] = False

        #     if ((nums[i-2]+1 == nums[i-1]) and (nums[i-1]+1 == nums[i])):
        #         # print(i, nums[i-2], nums[i-1], nums[i])
        #         isvalidcache[i+1] = 3
        #         validarray[i+1] =  validarray[i-2] 
        #     else:
        #         if (nums[i-1] == nums[i]):
        #             isvalidcache[i+1] = 1
        #             validarray[i+1] =  validarray[i-1]

        #         if (isvalidcache[i] in [1,2] and nums[i-1] == nums[i]):
        #             # print(i, nums[i-2], nums[i-1], nums[i], isvalidcache[i])
        #             isvalidcache[i+1] = 2
        #             validarray[i+1] =   validarray[i-1] or validarray[i-2]

        #         # if (isvalidcache[i]== 2 and nums[i-1] == nums[i]):
        #         #     # print(i, nums[i-2], nums[i-1], nums[i], isvalidcache[i])
        #         #     isvalidcache[i+1] = 2
        #         #     validarray[i+1] =  validarray[i+1] or validarray[i-2]


        # print(isvalidcache)
        # print(validarray)

        # return validarray[n]

            


        
