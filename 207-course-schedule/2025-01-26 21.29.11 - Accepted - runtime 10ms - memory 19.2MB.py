from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build an adjacency list
        # do dfs from each node, use a visited set to keep track of all nodes in the cur path to detect a cycle
        # after visiting all children of a node, remove it from visited and 
        # also del all it's prereqs from adj list so you know that course can be taken without visiting it's children.
        adjList = defaultdict(list)

        for [course, prereq] in prerequisites:
            adjList[course].append(prereq)

        def hasCycle(node, visited):
            if node in visited:
                return True
            visited.add(node)
            res = False
            for neighbor in adjList[node]:
                res = res or hasCycle(neighbor, visited)
            visited.remove(node)
            adjList[node] = []

            return res
        
        for course in range(numCourses):
            if hasCycle(course, set()):
                return False

        return True
            
        


