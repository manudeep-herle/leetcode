class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mem = [0] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                mem[i] = mem[i-1]
                continue
            j = i-1
            while True:
                if j < 0:
                    break
                if nums[j] < nums[i]:
                    mem[i] = max(mem[j] + 1, mem[i])
                    if mem[i] >= 2:
                        return True
                if nums[j] == nums[i]:
                    mem[i] = max(mem[j], mem[i])
                    break

                j -= 1
        # print(mem)
        return False


