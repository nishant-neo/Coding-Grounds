"""
115. Distinct Subsequences
Solved
Hard
Topics
Companies
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n_s, n_t = len(s), len(t)
        @cache
        def lcs(it_s, it_t):
            if it_t == n_t:
                return 1
            if it_s == n_s:
                return 0

            if s[it_s] == t[it_t]:
                return lcs(it_s+1, it_t+1) + lcs(it_s+1, it_t)
            else:
                return lcs(it_s+1, it_t)

        return lcs(0, 0)

    # def numDistinct(self, s: str, t: str) -> int:
    #     n_s, n_t = len(s), len(t)
    #     lcs = [[ 0 for i in range(n_t+1)] for j in range(n_s+1)]
        
    #     for i in range(n_s+1):
    #         lcs[i][n_t] = 1

    #     for i in reversed(range(0, n_s)):
    #         for j in reversed(range(0,n_t)):
    #             lcs[i][j] = lcs[i+1][j]

    #             if s[i] == t[j]:
    #                 lcs[i][j] += lcs[i+1][j+1]
                
    #     return lcs[0][0]

        
