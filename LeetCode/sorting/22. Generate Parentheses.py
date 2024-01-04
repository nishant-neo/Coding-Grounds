"""
22. Generate Parentheses
Solved
Medium

Topics

Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results, self.result = [], ''
        def dfs(opened, closed):
            if opened > n:
                return
            if opened == n and closed == n:
                self.results.append(str(self.result))
                return

            if opened <= n:
                self.result += '('
                dfs(opened+1, closed)
                self.result = self.result[:-1]
            if opened > closed:
                self.result += ')'
                dfs(opened, closed+1)
                self.result = self.result[:-1]

            # return

        dfs(0, 0)

        return self.results
