"""
212. Word Search II
Solved
Hard
Topics
Companies
Hint
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.isword = False

    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word
        cur.isword = True
            

class Solution:
 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addword(w)

        res, visited = set(), set()
        def dfs(r, c, node):
            # print(r, c, node.children.keys())
            node = node.children[board[r][c]]
            visited.add((r,c))
            if node.isword:
                node.isword = False
                res.add(node.word)

            for dr,dc in [(1,0), (0,1), (-1, 0),(0,-1)]:
                _r, _c = r+dr, c+dc

                if (_r in range(ROW) and 
                    _c in range(COL) and 
                    (_r, _c) not in visited and
                    board[_r][_c] in node.children
                    ):
                    dfs(_r, _c, node)

            visited.remove((r,c))


        for r in range(ROW):
            for c in range(COL):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res

        

        
