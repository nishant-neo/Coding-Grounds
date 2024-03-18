"""
1494. Parallel Courses II
Solved
Hard
Topics
Companies
Hint
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semesters for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is possible to take every course.

 

Example 1:


Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.
Example 2:


Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph.
In the first semester, you can only take courses 2 and 3 since you cannot take more than two per semester.
In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.
 

Constraints:

1 <= n <= 15
1 <= k <= n
0 <= relations.length <= n * (n-1) / 2
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
The given graph is a directed acyclic graph.
"""

from itertools import combinations # for picking k of n
class Solution:
    @lru_cache(None) # caching for faster lookups
    def recurse(self, mask, in_degrees):
        # if all the bits are 0, we have taken all the courses
        if not mask: return 0
        
        # all the nodes that *can* be taken now, following both the properties
        nodes = [i for i in range(self.n) if mask & 1 << i and in_degrees[i] == 0]
        
        ans = float('inf')
        # enumerating all the possible combinations
        for k_nodes in combinations(nodes, min(self.k, len(nodes))):
            new_mask, new_in_degrees = mask, list(in_degrees)
            
            # updating what would happen to new_mask and new_in_degrees 
            # if we considered the nodes in k_nodes
            for node in k_nodes:
                # since we know the bit is set, we un-set this bit, to mark it "considered"
                new_mask ^= 1 << node
                # updating each of the in-degrees, since the "parents" have been taken away
                for child in self.graph[node]:
                    new_in_degrees[child] -= 1
            
            # the heart of recursion
            # note the +1!
            ans = min(ans, 1+self.recurse(new_mask, tuple(new_in_degrees)))
        return ans
    
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # saving n and k for later use
        self.n = n
        self.k = k
        in_degrees = [0]*self.n
        # graph layout remains the same, although the in_degrees change. 
        # This allows us to keep graph as self.graph 
        # instead of passing it over and over.
        self.graph = defaultdict(list)
        for prev_course, next_course in relations:
            # remember, its 0-indexed now!
            in_degrees[next_course - 1] += 1
            self.graph[prev_course - 1].append(next_course - 1)
        
        # start with all the bits set
        return self.recurse((1 << self.n) - 1, tuple(in_degrees))
