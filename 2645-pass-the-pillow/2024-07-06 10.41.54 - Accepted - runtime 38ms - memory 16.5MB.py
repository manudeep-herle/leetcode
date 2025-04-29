class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = (time) // (n-1) 
        pos = (time) % (n-1)
        print(rounds, pos)
        if rounds % 2 == 0:
            return pos + 1
        else:
            return n - pos
        