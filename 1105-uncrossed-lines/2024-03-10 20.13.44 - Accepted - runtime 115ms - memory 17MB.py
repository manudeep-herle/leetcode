class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        mem = [([0] * (n1+1)) for _ in range(n2+1)]
        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if nums2[i-1] == nums1[j-1]:
                    mem[i][j] = mem[i-1][j-1] + 1
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j-1])
        return max(mem[-1])
        