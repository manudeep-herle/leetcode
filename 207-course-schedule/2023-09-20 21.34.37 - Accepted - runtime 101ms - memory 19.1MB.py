class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph each course mapped to a list of prerequisites
        graph = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        rec_stack = set()

        def has_cycle(crs):
            # 
            if crs in rec_stack:
                return True
            # Course doesn't have any prerequisites
            if graph[crs] == []:
                return False

            rec_stack.add(crs)
            for pre in graph[crs]:
                if has_cycle(pre):
                    return True
            rec_stack.remove(crs)
            graph[crs] = []
            
            return False
        
        
        for crs in range(numCourses):
            if has_cycle(crs):
                return False
        return True