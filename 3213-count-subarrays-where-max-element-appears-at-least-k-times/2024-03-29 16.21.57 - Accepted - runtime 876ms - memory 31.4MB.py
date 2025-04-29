class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        big = max(nums)
        print(big)
        bigPos = deque()
        res = 0
        for rp, num in enumerate(nums):
            if num == big:
                bigPos.append(rp)
                if len(bigPos) > k:
                    bigPos.popleft()
            if len(bigPos) == k:
                res += bigPos[0] - 0 + 1
        return res
        