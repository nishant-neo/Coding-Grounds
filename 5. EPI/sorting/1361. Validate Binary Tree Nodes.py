"""
1361. Validate Binary Tree Nodes
Solved
Medium

Topics

Companies

Hint
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
 

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {}
        for idx, (leftchild, rightchild) in enumerate(zip(leftChild,rightChild)):
            if leftchild in parent or rightchild in parent:
                return False
            if leftchild != -1:
                parent[leftchild] = idx
            if rightchild != -1:
                parent[rightchild] = idx

        # print(parent)
    
        count = 0
        root = 0
        for i in range(n):
            if i not in parent:
                count += 1
                root = i
        
        if count != 1:
            return False 

        visited = set()
        queue = [root]

        
        while(len(queue)>0):
            # print(queue)
            node = queue.pop(0)
            visited.add(node)
            
            if leftChild[node] != -1:
                if leftChild[node] in visited:
                    return False
                queue.append(leftChild[node])

            if rightChild[node] != -1:
                if rightChild[node] in visited:
                    return False
                queue.append(rightChild[node])

        for i in range(n):
            if i not in visited:
                return False

        return True 


