"""
337. House Robber III
Solved
Medium

Topics

Companies
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # pure DP
        if not root:
            return 0
            
        # reform tree into array-based tree
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))

        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index+1)

        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index+1)

        for i in reversed(range(index+1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])

        return max(dp_rob[0], dp_not_rob[0])


        # Tree with memoization
        # rob_saved = {}
        # not_rob_saved = {}

        # def dfs(root, stole):
        #     if root is None:
        #         return 0

        #     if stole:
        #         if root in rob_saved:
        #             return rob_saved[root]
        #         rob_saved[root] = dfs(root.left, False)+dfs(root.right, False)
        #         return rob_saved[root]
        #     else:
        #         if root in not_rob_saved:
        #             return not_rob_saved[root]
        #         rob = (root.val + dfs(root.left, True)+dfs(root.right, True))
        #         not_rob = (dfs(root.left, False)+dfs(root.right, False))
        #         result = max(rob, not_rob)
        #         not_rob_saved[root] = result
        #         return not_rob_saved[root]
                
                
                
        # return dfs(root, False)
            
        
