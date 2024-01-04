"""
490. The Maze
Solved
Medium

Topics

Companies
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
"""

class Solution:
    def __init__(self):
        self.flag = False
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        
        visited = set()
        def dfs(r,c):
            if destination[0] == r and destination[1] == c:
                self.flag = True
                return
            if (r,c) in visited:
                return

            visited.add((r,c))

            for directions in [[1,0], [-1,0], [0,1], [0,-1]]:
                r_, c_ = r, c
                dx, dy = directions
                while(r_ in range(R) and c_ in range(C) and maze[r_][c_] == 0):
                    r_ += dx 
                    c_ += dy
                dfs(r_-dx, c_-dy)

        dfs(start[0],start[1])

        return self.flag
