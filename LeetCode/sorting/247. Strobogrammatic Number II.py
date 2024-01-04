"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]
 

Constraints:

1 <= n <= 14
"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = [[], ["0", "1", "8"], ["11", "69", "88", "96"]]
        if n < 3:
            return res[n]

        res = res + [[] for i in range(n-2)]

        for i in range(3, n+1):
            # print(f"i={i}")
            if i%2 != 0:
                result = []
                for a in res[1]:
                    for b in res[i-1]:
                        subsize = int((i-1)/2)
                        s_num = b[0:subsize] + a + b[subsize:]
                        result.append(s_num)
            
            if i%2 == 0:
                result = []
                for a in res[2]+["00"]: # since this is is not a valid number when n=2, but is valid for recursopn
                    for b in res[i-2]:
                        subsize = int((i-1)/2)
                        s_num = b[0:subsize] + a + b[subsize:]
                        result.append(s_num)

            
            res[i]=result


        return res[n]
        
