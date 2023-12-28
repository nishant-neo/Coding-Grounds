"""
2316. Count Unreachable Pairs of Nodes in an Undirected Graph
Solved
Medium

Topics

Companies

Hint
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

 

Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
 

Constraints:

1 <= n <= 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
"""

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        edge_adj_list = {i:[] for i in range(n)}
        for node_a, node_b in edges:
            edge_adj_list[node_a].append(node_b)
            edge_adj_list[node_b].append(node_a)
            
        visited = set()
        pairs = 0
        remaining_nodes = n
        def dfs(node, count):
            if node in visited:
                return

            visited.add(node)
            connected_components[count] += 1
            for adj_node in edge_adj_list[node]:
                dfs(adj_node, count)

        connected_components = {}
        count = 0
        for i in range(n):
            if i not in visited:
                connected_components[count] = 0
                dfs(i, count)
                pairs += (connected_components[count]) * (remaining_nodes-connected_components[count])
                remaining_nodes -= connected_components[count]
                count += 1

        # connected_components_len = [ len(v) for v in connected_components.values()]

        # for i in range(len(connected_components_len)):
        #     for j in range(i+1, len(connected_components_len)):
        #         pairs += connected_components_len[i]*connected_components_len[j]

        return pairs
