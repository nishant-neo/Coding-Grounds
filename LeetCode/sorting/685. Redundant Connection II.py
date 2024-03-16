"""
685. Redundant Connection II
Solved
Hard
Topics
Companies
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n
ui != vi

"""

class Solution:
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        nodes = 0
        for u, v in edges:
            nodes = max(nodes, u, v)

        parent = [ i for i in range(nodes+1)]
        rank = [0 for i in range(nodes+1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node_a, node_b):
            p_a, p_b = find(node_a), find(node_b)
            
            if p_a == p_b:
                return False
            else:
                if rank[p_a] > rank[p_b]:
                    parent[p_b] = p_a
                    rank[p_a] += rank[p_b]
                else:
                    parent[p_a] = p_b
                    rank[p_b] += rank[p_a]
            return True
        
        
        parent_relation = [0] * (nodes + 1)
        candidate1, candidate2 = None, None
        
        for edge in edges:
            u, v = edge
            if parent_relation[v] == 0:
                parent_relation[v] = u
            else:
                candidate1 = [parent_relation[v], v]
                candidate2 = edge
                

        for edge in edges:
            u, v = edge
            if edge == candidate2:
                continue
            # If the union() method returns False, then we have found a cycle in the graph, 
            # and we can return candidate1 if it is not None, 
            # otherwise we return the current edge (i.e. [u, v]).
            if not union(u, v):
                return candidate1 if candidate1 else edge

        # If we have not found a cycle by the end of the loop, 
        # then the graph must be a tree with a node with two parents. 
        # In this case, we can return candidate2.

        return candidate2

        
