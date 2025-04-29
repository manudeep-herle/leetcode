class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        hmap = {}

        for r in range(len(nums)-1, -1, -1):
            for c in range(len(nums[r])):
                if r+c not in hmap:
                    hmap[r+c] = []
                hmap[r+c].append(nums[r][c])
        k = 0
        while k in hmap:
            res += hmap[k]
            k += 1

        return res

