from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the graph and the indegree array
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for prereq, course in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Perform topological sort
        queue = deque()
        for course in indegree:
            if indegree[course] == 0:
                queue.append(course)
        
        totalCourses = 0
        while queue:
            course = queue.popleft()
            totalCourses += 1
            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        return totalCourses == numCourses