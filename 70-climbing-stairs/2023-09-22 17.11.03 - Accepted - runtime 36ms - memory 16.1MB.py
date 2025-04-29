class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
            
        mem = {}

        def recurse(curr_steps):

            if curr_steps == n:
                return 1
            if curr_steps > n:
                return 0

            if curr_steps in mem:
                return mem[curr_steps]
            else:
                mem[curr_steps] = recurse(curr_steps+1) + recurse(curr_steps+2)
                return mem[curr_steps]
        
        return recurse(0)
        