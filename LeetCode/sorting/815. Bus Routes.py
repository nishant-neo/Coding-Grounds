"""
815. Bus Routes
Solved
Hard
Topics
Companies
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        stop_in_bus_routes = defaultdict(list)
        for idx, route in enumerate(routes):
            for stop in route:
                stop_in_bus_routes[stop].append(idx)

        adj_list = defaultdict(set)
        for idx, route in enumerate(routes):
            for stop in route:
                adj_list[idx].update(stop_in_bus_routes[stop])


        sources = stop_in_bus_routes[source]
        targets = stop_in_bus_routes[target]

        queue = sources
        hops = 1
        visited = set()
        while( len(queue) > 0):
            to_be_popped = len(queue)

            for _ in range(to_be_popped):
                node = queue.pop(0)
                if node in targets:
                    return hops
                visited.add(node)

                for adj_node in adj_list[node]:
                    if adj_node not in visited:
                        queue.append(adj_node)
            
            hops += 1

        return -1


        
