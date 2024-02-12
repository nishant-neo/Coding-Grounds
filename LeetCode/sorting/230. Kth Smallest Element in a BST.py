"""
230. Kth Smallest Element in a BST
Solved
Medium
Topics
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        time: O(n), space: O(n)
        """
        
        def helper(root, values):
            if root is None:
                return

            helper(root.left, values)
            values.append(root.val)
            helper(root.right, values)

        values = []
        helper(root, values)
        return values[k - 1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        time: O(n), space: O(h)
        """
        
        self.res = 0
        self.count = 0
        def helper(root):
            if root is None or self.count >= k:
                return
            helper(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return 
            helper(root.right)

        helper(root)
        return self.res





            

        





            

        
