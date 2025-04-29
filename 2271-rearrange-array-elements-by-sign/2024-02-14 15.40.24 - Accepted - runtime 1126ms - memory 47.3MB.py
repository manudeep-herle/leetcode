class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0,0
        res = [-1]
        while len(res) < len(nums)+1:
            if res[-1] < 0:
                if nums[pos] >= 0:
                    res.append(nums[pos])
                pos += 1
            else:
                if nums[neg] < 0:
                    res.append(nums[neg])
                neg += 1
        return res[1:]
                
        