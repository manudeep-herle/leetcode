class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        start_courses = set()
        graph = [[] for _ in range(numCourses)]
        
        for [e,s] in prerequisites:
            if e == s:
                return False
            graph[s].append(e)

        recursion_stack = []
        visited = set()

        def dfs(node):
            recursion_stack.append(node)
            visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    if dfs(neigh):
                        return True
                elif neigh in recursion_stack:
                    return True
            
            recursion_stack.pop()
                
        # print(graph, start_courses)
        for course in range(numCourses):
            if dfs(course): # if cycle return false
                print(course)
                return False 
        return True # if no cycle return true


        # Check if there's a cycle
        # Check if all the vertices are reachable
        