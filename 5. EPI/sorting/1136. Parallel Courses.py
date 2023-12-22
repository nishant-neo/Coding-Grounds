"""
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
"""
class Solution:
    def __init__(self):
        self.semester_needed = {}
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjlist= {i+1:[] for i in range(n)}
        # print()
        for prevcourse, nextcourse in relations:
            adjlist[nextcourse].append(prevcourse)
        

        visited = set()
        def dfs(course):
            # print(course, self.semester_needed)
            if course in self.semester_needed:
                return self.semester_needed[course]
            
            visited.add(course)
            max_semester = 0

            for _course in adjlist[course]:
                if _course not in visited:
                    if _course not in self.semester_needed:
                        self.semester_needed[_course] = dfs(_course)
                    max_semester = max(max_semester, self.semester_needed[_course])
                else:
                    self.semester_needed[course] = -1
                    return self.semester_needed[course]
            visited.remove(course)        
            self.semester_needed[course] = max_semester+1
        

            return self.semester_needed[course]

        max_semester = -1
        for i in range(0,n):
            # print("startt", i+1)
            sems_reqd = dfs(i+1)
            if sems_reqd == -1:
                return -1
            max_semester = max(max_semester, sems_reqd)

        # print(self.semester_needed)

        return max_semester
