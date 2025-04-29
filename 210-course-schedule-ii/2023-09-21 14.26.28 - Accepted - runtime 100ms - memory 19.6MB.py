class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build a graph from prerequisites
        graph = {pre: [] for pre in range(numCourses) }
        res = []
        stack = set()
        visited = set()


        for crs, pre in prerequisites:
            graph[pre].append(crs)

        print(graph)

        
        # return true if there's a cycle, add topological sort to res
        def dfs(pre):
            if pre in stack:
                return True
            if pre in visited:
                return False


            stack.add(pre)
            visited.add(pre)

            for crs in graph[pre]:
                if dfs(crs):
                    return True

            stack.remove(pre)
            res.append(pre)
        
        # Do a topological sort
        for pre in graph:
            if dfs(pre):
                return []
        
        return res[::-1]
            
        