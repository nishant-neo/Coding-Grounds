"""
1727. Largest Submatrix With Rearrangements
Solved
Medium

Topics

Companies

Hint
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
"""

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        subsequence = [[0 for i in range(C)] for i in range(R)]

        for col in range(C):
            for row in range(R):
                if row == 0:
                    subsequence[row][col] = matrix[row][col]
                else:
                    subsequence[row][col] = (subsequence[row-1][col]+1) if matrix[row][col] == 1 else 0


        largest_matrix = 0        
        for row in range(R):
            
            # Without Sorting but slow
            row_set = set(subsequence[row])
            matrix_size  = 0
            for r_set in row_set:
                for col in range(C):
                    if subsequence[row][col] >= r_set:
                        matrix_size += min(r_set, subsequence[row][col])
                largest_matrix = max(largest_matrix, matrix_size)
                matrix_size  = 0

            # Sorting, also slow
            # sorted_row = sorted(subsequence[row], reverse=True)
            # for i in range(C):
            #     largest_matrix = max(largest_matrix, sorted_row[i] * (i + 1))
        
        return largest_matrix


        # O(R*C) Solution

        m = len(matrix)
        n = len(matrix[0])
        prev_heights = []
        ans = 0

        for row in range(m):
            heights = []
            seen = [False] * n
            
            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    seen[col] = True

            for col in range(n):
                if seen[col] == False and matrix[row][col] == 1:
                    heights.append((1, col))
            
            for i in range(len(heights)):
                ans = max(ans, heights[i][0] * (i + 1))
                
            prev_heights = heights

        return ans
                

        
