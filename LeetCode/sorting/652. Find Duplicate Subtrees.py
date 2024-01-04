"""
652. Find Duplicate Subtrees
Solved
Medium

Topics

Companies
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        result, lookup = [], {}
        def inorder(node, representation):
            if node is None:
                return ""

            l_rep, r_rep = [], []
            if node.left:
                l_rep = inorder(node.left, representation)
            if node.right:
                r_rep = inorder(node.right, representation)
            
            representation_in_str = (
                "(" + "".join([str(n) for n in l_rep]) + ")" +
                str(node.val) + 
                "(" + "".join([str(n) for n in r_rep]) + ")" 
            )
            
            if representation_in_str in lookup and lookup[representation_in_str] == 1:
                result.append(node)
            
            lookup[representation_in_str] = lookup.get(representation_in_str, 0) + 1

            return representation_in_str

        inordertraversal = inorder(root, [])
        # print(inordertraversal, result)

        return result
        
