class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0
        
        while i < len(asteroids):
            ast = asteroids[i]
            if ast > 0:
                st.append(ast)
                i += 1
            else:
                if len(st) == 0 or st[-1] < 0:
                    st.append(ast)
                    i += 1
                elif st[-1] > abs(ast):
                    i += 1
                    continue
                elif st[-1] < abs(ast):
                    st.pop()
                elif st[-1] == abs(ast):
                    st.pop() 
                    i += 1

        return st
                
        