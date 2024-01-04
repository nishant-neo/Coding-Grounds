"""
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
"""
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heights = {}
        def get_height(node):
            if not node:
                return -1
            height = 1+max(get_height(node.left),get_height(node.right))
            # caching the heights to be reused
            heights[node.val] = height
            return height

        get_height(root)  


        heights_ = {}

        def dfs(root, depth, max_val):
            if root is None:
                return 

            # for root, should be zero, if root is removed, height = 0
            heights_[root.val] = max_val

            # here we find the height without the current node
            # so for left, it will be the height considering only its sibling (which is right st)
            
            # without caching, got me TLE
            # dfs(root.left, depth+1, max(max_val, depth+1+get_height(root.right)))
            # dfs(root.right, depth+1, max(max_val, depth+1+get_height(root.left)))

            dfs(root.left, depth+1, max(max_val, depth+1+(heights[root.right.val] if root.right else -1)))
            dfs(root.right, depth+1, max(max_val, depth+1+(heights[root.left.val] if root.left else -1)))


        dfs(root, 0, 0)

        return [ heights_[q] for q in queries]
