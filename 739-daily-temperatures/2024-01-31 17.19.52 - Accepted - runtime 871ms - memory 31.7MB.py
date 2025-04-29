class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temperatures)
        indices = []

        for i in range(len(temperatures)):



            while st and temperatures[i] > st[-1]:
                st.pop()
                j = indices.pop()
                ans[j] = i-j

            st.append(temperatures[i])
            indices.append(i)

            

            
        
        return ans

            