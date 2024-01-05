"""
79. Word Search
Solved
Medium

Topics

Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        visited = set()
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            # print(i, j , idx, word[idx], board[i][j])
            if word[idx] != board[i][j]:
                return False 

            if idx+1 == len(word):
                return True

            visited.add((i, j))
            
            status = False
            for di,dj in [(-1,0), (1,0), (0,1), (0,-1)]:
                i_ = i+di
                j_ = j+dj

                if (
                    (i_, j_) not in visited and
                    i_ in range(m) and
                    j_ in range(n)
                ):
                    status =  status or dfs(i_, j_, idx+1)

            visited.remove((i, j))


            return status


        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True

        return False

        
