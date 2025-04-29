class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean):
            neighs = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            
            for [r_, c_] in neighs:
                if (r_, c_) in ocean or r_ >= R or r_ < 0 or c_ >= C or c_ < 0:
                    continue

                if heights[r_][c_] >= heights[r][c]:
                    ocean.add((r_, c_))
                    dfs(r_, c_, ocean)
        
        # Top row
        r = 0
        for c in range(C):
            pacific.add((r,c))
            # Check all cells reachable by (r,c) add em to pacific
            dfs(r,c, pacific)
        
        # Left column
        c = 0
        for r in range(R):
            pacific.add((r,c))
            dfs(r,c, pacific)

        # Bottom row
        r = R - 1
        for c in range(C):
            atlantic.add((r,c))
            # Check all cells reachable by (r,c) add em to pacific
            dfs(r,c, atlantic)

        # Right column
        c = C - 1
        for r in range(R):
            atlantic.add((r,c))
            dfs(r,c, atlantic) 

        print(atlantic)       

        return pacific.intersection(atlantic)

