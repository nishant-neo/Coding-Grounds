"""
2116. Check if a Parentheses String Can Be Valid
Solved
Medium

Topics

Companies

Hint
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
 

Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
"""


class Solution:
    def __init__(self):
        self.status = False
        self.res = ""
        
    def canBeValid(self, s: str, locked: str) -> bool:

        # if len(s) % 2 != 0:
        #     return False
        
        def validate(s, locked, op):
            """
            From left to right, if a locked ')' is encountered, it must be balanced 
            with either a locked '(' or an unlocked index on its left.

            Similarly for '(', from right to left
            """
            bal, wild = 0, 0 
            for i in range(len(s)):
                if locked[i] == '1':
                    # if a locked ')' is encountered, it must be balancing with a locked '('
                    bal+=-1 if s[i]==op else 1
                else:
                    # balancing it with unlocked index
                    wild += 1
                if wild+bal < 0:
                    return False
            return bal <= wild

        return len(s) % 2 == 0 and validate(s, locked, ')') and validate(s[::-1], locked[::-1], '(')
            

        # DFS timeout

        # def isvalid(s):
        #     if s == '(' or s == ')':
        #         return False

        #     n = len(s)
        #     for i in range(int(n/2)):
        #         if s[i] != s[n-i-1]:
        #             return False
            
        #     return True

        # def dfs(i, open_p):
        #     if i == len(s):
        #         # print(self.res)
        #         self.status = isvalid(self.res) or self.status
        #         return 
        #     # print(i, open_p, locked[i])
        #     if locked[i]==1:
        #         self.res = self.res + s[i]
        #         delta = (1 if s[i] == '(' else -1)
        #         dfs(i+1, open_p+delta)
        #     else:
        #         # print(i, open_p)
        #         if open_p <= 0:
        #             self.res = self.res + '('
        #             dfs(i+1, open_p+1)
        #         else:
        #             self.res = self.res + '('
        #             dfs(i+1, open_p+1)
        #             self.res = self.res[:-1]
        #             self.res = self.res + ')'
        #             dfs(i+1, open_p-1)

        # if s[0] == '(':
        #     dfs(0, 1)
        # else:
        #     dfs(0, -1)

        # return self.status




        
