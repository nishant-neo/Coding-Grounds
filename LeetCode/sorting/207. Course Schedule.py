"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_adj_list = {}
        for pre in prerequisites:
            if pre[0] in pre_adj_list:
                pre_adj_list[pre[0]].append(pre[1])
            else:
                pre_adj_list[pre[0]] = [pre[1]]

        
        course_flag = {}

        def dfs(i):
            if i in visited:
                return False
            if i in course_flag:
                return course_flag[i]

            visited.add(i)
            status = True
            
            if i in pre_adj_list:
                for courses in pre_adj_list[i]: 
                    status = status and dfs(courses)

            visited.remove(i)
            course_flag[i] = status
            return status


        for i in range(numCourses):
            visited=set()
            flag = dfs(i)
            if not flag:
                return False

        return True
        
