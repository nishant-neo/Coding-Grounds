"""
118. Pascal's Triangle
Solved
Easy

Topics

Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascal_triangle = [[1], [1,1]]

        if numRows <= 2:
            return pascal_triangle[0:numRows]

        for n in range(2, numRows):
            new_entry = [1]
            last_entry = pascal_triangle[n-1]
            for idx in range(1, len(last_entry)):
                new_entry.append(last_entry[idx]+last_entry[idx-1])
            new_entry.append(1)

            pascal_triangle.append(new_entry)

        # print(pascal_triangle)

        return pascal_triangle

        
