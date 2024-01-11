"""
399. Evaluate Division
Solved
Medium

Topics

Companies

Hint
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq_adj = {}
        eq_val = {}
        varbls = set()
        for (eq_1, eq_2), val in zip(equations, values):
            eq_val[(eq_1, eq_2)] = val
            eq_val[(eq_2, eq_1)] = 1/val
            varbls.add(eq_1)
            varbls.add(eq_2)
            if eq_1 in eq_adj:
                eq_adj[eq_1].append(eq_2)
            else:
                eq_adj[eq_1] = [eq_2]

            if eq_2 in eq_adj:
                eq_adj[eq_2].append(eq_1)
            else:
                eq_adj[eq_2] = [eq_1]
        # print(eq_adj, eq_val)


        stack = equations
        visited = set()
        marked = set()
        def dfs(node):
            if (node[0], node[1]) in marked:
                return
            if node[0] == node[1]:
                return 
            # print("node", node)
            marked.add((node[0], node[1]))
            visited.add(node[0])
            visited.add(node[1])
            
            if node[1] in eq_adj:
                # print(eq_adj[node[1]])
                for next_node in eq_adj[node[1]]:
                    
                    if next_node in visited:
                        continue
        
                    if node[0] in eq_adj:
                        eq_adj[node[0]].append(next_node)
                    else:
                        eq_adj[node[0]] = [next_node]

                    eq_val[(node[0], next_node)] = eq_val[(node[0], node[1])] * eq_val[(node[1], next_node)]
                    dfs([node[0], next_node])
            # print(visited)
            if node[0] in visited:
                visited.remove(node[0])
            if node[1] in visited:
                visited.remove(node[1])

            

        for equation in equations:
            dfs(equation)

        for equation in equations:
            dfs((equation[1],equation[0]))


        result = []
        for query in queries:
            query = (query[0], query[1])
            rev_query = (query[1], query[0])
            if query[0] == query[1] and query[0] in varbls:
                result.append(1.0)
            elif query in eq_val:
                result.append(eq_val[query])
            else:
                result.append(-1.0)


        
        # print(eq_adj, eq_val)
        return result
