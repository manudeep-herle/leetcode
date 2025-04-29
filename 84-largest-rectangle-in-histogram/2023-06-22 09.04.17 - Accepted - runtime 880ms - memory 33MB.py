class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        maxHeight = 0 

        i = -1
        for height in heights:
            
            i += 1
            if not st or height >= st[-1][1]:
                st.append(( i, height))
            
            else:

                while st and height < st[-1][1]:
                    l = st.pop()
                    h = l[1] * (i - l[0])
                    
                    if h > maxHeight:
                        maxHeight = h
                
                st.append((l[0], height))
        
        i += 1
        while st:
            l = st.pop()
            h = l[1] * (i - l[0])
            
            if h > maxHeight:
                maxHeight = h
        
        return maxHeight
