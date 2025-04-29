class Solution:
    def hammingWeight(self, n: int) -> int:
        uint = '{0:032b}'.format(n)
        print(uint, len(uint))
        count = 0
        for i in range(len(uint)):
            if uint[i] == '1':
                count += 1
        return count