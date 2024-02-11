"""
2973. Find Number of Coins to Place in Tree Nodes
Solved
Hard
Topics
Companies
Hint
You are given an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array cost of length n, where cost[i] is the cost assigned to the ith node.

You need to place some coins on every node of the tree. The number of coins to be placed at node i can be calculated as:

If size of the subtree of node i is less than 3, place 1 coin.
Otherwise, place an amount of coins equal to the maximum product of cost values assigned to 3 distinct nodes in the subtree of node i. If this product is negative, place 0 coins.
Return an array coin of size n such that coin[i] is the number of coins placed at node i.

 

Example 1:


Input: edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
Output: [120,1,1,1,1,1]
Explanation: For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
Example 2:


Input: edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
Output: [280,140,32,1,1,1,1,1,1]
Explanation: The coins placed on each node are:
- Place 8 * 7 * 5 = 280 coins on node 0.
- Place 7 * 5 * 4 = 140 coins on node 1.
- Place 8 * 2 * 2 = 32 coins on node 2.
- All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
Example 3:


Input: edges = [[0,1],[0,2]], cost = [1,2,-2]
Output: [0,1,1]
Explanation: Node 1 and 2 are leaves with subtree of size 1, place 1 coin on each of them. For node 0 the only possible product of cost is 2 * 1 * -2 = -4. Hence place 0 coins on node 0.
 

Constraints:

2 <= n <= 2 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
cost.length == n
1 <= |cost[i]| <= 104
The input is generated such that edges represents a valid tree.
"""

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        adj_list = {i:[] for i in range(n)}
        for n_a, n_b in edges:
            adj_list[n_a].append(n_b)
            adj_list[n_b].append(n_a)

        visited = set()

        @cache
        def dfs(node):
            # print(node)
            visited.add(node)
            top_nodes, top_neg_nodes = [], []
            if cost[node] > 0:
                top_nodes.append(cost[node])
            else:
                top_neg_nodes.append(cost[node])

            if len(adj_list[node]) == 0:
                return top_nodes, top_neg_nodes

            else:
                for adj_nodes in adj_list[node]:
                    if adj_nodes not in visited:
                        temp, temp_neg = dfs(adj_nodes)
                        top_nodes += temp
                        top_neg_nodes += temp_neg

                top_nodes.sort(reverse=True)
                top_neg_nodes.sort()
                if len(top_nodes) > 3:
                    top_nodes = top_nodes[0:3]
                if len(top_neg_nodes) > 2:
                    top_neg_nodes = top_neg_nodes[0:3]


                if len(top_nodes+top_neg_nodes) < 3:
                    res[node] = 1
                else:
                    if len(top_nodes) >= 3:
                        res[node] = prod(top_nodes)
                        if len(top_neg_nodes) >= 2:
                            res[node] = max(res[node], top_nodes[0]*prod(top_neg_nodes[0:2]))

                    elif len(top_nodes) == 2:
                        res[node] = 0
                        if len(top_neg_nodes) >= 2:
                            res[node] = max(res[node], top_nodes[0]*prod(top_neg_nodes[0:2]))

                    elif len(top_nodes) == 1:
                        res[node] = max(res[node], top_nodes[0]*prod(top_neg_nodes[0:2]))

                    else:
                        res[node] = 0
                
                return top_nodes, top_neg_nodes

        res = [0]*n
        
        top_nodes, top_neg_nodes = dfs(0)

        return res
