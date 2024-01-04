"""
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.
"""
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Clearly backtracking leads to TLE
        # How can we reduce the number of recursion?
        # We start with all the candidates
        # We evaluate every (i, j) where j>i and j, i are from candidates
        # And get the every number that is possible with (i,j), use that and rest of remaining candidate, recur
        # In the end we will left with one candidate, if that == 24 
        # @cache
        def operation(x, y):
            ans = [x+y, x-y, y-x, x*y]
            if x:
                ans.append(y / x)
            if y:
                ans.append(x / y)
            
            return ans
    
        def dfs(candidates):
            if len(candidates) == 1:
                return abs(candidates[0] - 24) < 0.001

            for i in range(len(candidates) - 1):
                for j in range(i+1, len(candidates)):

                    new_candidates = [val for idx, val in enumerate(candidates) if idx != i and idx != j]
                    new_list = operation(candidates[i], candidates[j])
                    for num in new_list:
                        if dfs(new_candidates + [num]):
                            return True
            return False

        return dfs(cards)




        
        # def dfs(i, value, target):
        #     if value == target:
        #         self.res = True
        #         return 
            
        #     if i >= len(cards):
        #         return

        #     # dfs(i+1, value + cards[i], target)
        #     # dfs(i+1, value - cards[i], target)
        #     # dfs(i+1, value * cards[i], target)
        #     # dfs(i+1, value / cards[i], target)

        #     dfs(i, 1, target-(value))
        #     dfs(i, 1, target+(value))
        #     dfs(i, 1, target/(value))
        #     dfs(i, 1, target*(value))

        # dfs(0, 1, 24)

        # return self.res

        
