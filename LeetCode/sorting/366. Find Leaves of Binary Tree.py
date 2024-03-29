"""
366. Find Leaves of Binary Tree
Solved
Medium

Topics

Companies
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        leaves = []
        def dfs(node):
            if node is None:
                return None

            if node.left is None and node.right is None:
                leaves.append(node.val)
                node = None
                return node
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)
            return node

        while(root):
            leaves =[]
            root = dfs(root)
            result.append(leaves)

        return result


    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        height_to_nodeval = {}
        def dfs(node):
            if node is None:
                return 0

            height = 0
            if not(node.left is None and node.right is None):
                node_left_height, node_right_height = 0,0
                if node.left:
                    node_left_height = dfs(node.left)
                if node.right:
                    node_right_height = dfs(node.right)
                height = 1+max(node_right_height, node_left_height)

            if height in height_to_nodeval:
                height_to_nodeval[height].append(node.val)
            else:
                height_to_nodeval[height] = [node.val]

            return height

        dfs(root)


        return height_to_nodeval.values()
