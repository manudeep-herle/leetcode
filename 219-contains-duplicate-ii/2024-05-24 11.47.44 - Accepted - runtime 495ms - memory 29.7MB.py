class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(int)
        l=r=0
        while r < len(nums):
            if r - l > k:
                hmap[nums[l]] -= 1
                l += 1
            if  hmap[nums[r]] > 0:
                return True
            hmap[nums[r]] += 1
            r += 1
        return False
