"""
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0]*n
        righttmax = [0]*n
        
        leftmax[0] = height[0]
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], height[i])

        righttmax[-1] = height[-1]
        for i in reversed(range(0,n-1)):
            righttmax[i] = max(righttmax[i+1],  height[i])

        water_trapped = 0
        for i in range(n):
            water_trapped += min(leftmax[i], righttmax[i])-height[i]


        return water_trapped

        
