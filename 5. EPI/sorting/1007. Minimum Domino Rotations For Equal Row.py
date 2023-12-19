"""
1007. Minimum Domino Rotations For Equal Row
Solved
Medium

Topics

Companies
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.


"""

class Solution:
    def __init__(self):
        self.min_rotations = 999999
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        nlen = len(tops)
        topC = Counter(tops)
        bottomC = Counter(bottoms)
        totalC = topC + bottomC

        num, freq = totalC.most_common()[0]

        for i in range(nlen):
            if num != tops[i] and num != bottoms[i]:
                return -1

        return nlen-max(topC[num], bottomC[num])

        # def dfs(i, rotations):
        #     if i == (len(tops)):
        #         print(tops.copy(), bottoms.copy())
        #         print("rotations", rotations)
        #         self.min_rotations = min(self.min_rotations, rotations)
        #         return
        #     # print("i=",i, "rotations = ", rotations)
        #     if i <= 1:
        #         dfs(i+1, rotations)
        #         tops[i], bottoms[i] = bottoms[i], tops[i]
        #         dfs(i+1, rotations+1)
 
        #     else:
        #         print(tops[i-1], tops[i], bottoms[i-1], bottoms[i])
        #         if (tops[i-1] == tops[i] == tops[i-2]) or (bottoms[i-1] == bottoms[i] == bottoms[i-2]):
        #             dfs(i+1, rotations)
        #         elif (
        #             ((tops[i-1] == tops[i-2]) and (tops[i-1] == bottoms[i])) or
        #             ((bottoms[i-1] == bottoms[i-2]) and (bottoms[i-1] == tops[i])) 
        #         ):
        #             print(i, tops, bottoms)
        #             tops[i], bottoms[i] = bottoms[i], tops[i]
        #             dfs(i+1, rotations+1)
        #         else:
        #             # print("return")
        #             return                

        # dfs(0, 0)

        return self.min_rotations if self.min_rotations != 999999 else -1
