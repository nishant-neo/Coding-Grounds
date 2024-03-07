"""
878. Nth Magical Number
Solved
Hard
Topics
Companies
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
 

Constraints:

1 <= n <= 109
2 <= a, b <= 4 * 104
"""

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        low = min(a, b)
        high = n*low
        lcm = math.lcm(a, b)

        # to find the index of magic number is
        # f(x) = x//a + x//b - x//lcm(a,b)
        # now all we have to do is find the right x, given index=n
        # we use bin-search for that
        while (low <= high):
            mid = low + (high-low)//2
            if (mid//a) + (mid//b) - (mid//lcm) < n:
                low = mid+1
            else:
                high = mid-1
                
        return low % MOD
        
