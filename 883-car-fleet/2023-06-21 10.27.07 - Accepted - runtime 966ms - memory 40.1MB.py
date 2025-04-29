class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = len(position)

        # Convert two lists into a list of sets
        los = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            los.append((position[i], speed[i], time))

        # sort by position
        los.sort(key = lambda s: s[0])

        # Now find the number of fleets
        st = []
        for car in los:
            # while car reaches later than prev car on stack
            while st and car[2] >= st[-1][2]: 
                ans -= 1 # 1 fewer fleet
                st.pop()

            st.append(car)


        return ans