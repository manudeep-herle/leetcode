class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build a graph from prerequisites
        graph = {pre: [] for pre in range(numCourses) }
        res = []
        stack = set()


        for crs, pre in prerequisites:
            graph[pre].append(crs)

        print(graph)

        
        # return true if there's a cycle, add topological sort to res
        def dfs(pre):
            if graph[pre] == []:
                if pre not in res:
                    res.append(pre)
                return False
            
            # if this course is already in the stack, there's a cycle in the graph
            if pre in stack:
                return True
            
            stack.add(pre)

            for crs in graph[pre]:
                if dfs(crs):
                    return True
            
            stack.remove(pre)
            res.append(pre)

            # No need to recurse again if we encounter a node we've visited before and which doesn't lead to a cycle.
            graph[pre] = []


        
        # Do a topological sort
        for pre in graph:
            if dfs(pre):
                return []
        
        return res[::-1]
            
        