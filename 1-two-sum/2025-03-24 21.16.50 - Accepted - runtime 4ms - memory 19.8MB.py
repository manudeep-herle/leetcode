class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time = space = O(n)
        # iterate through nums, create a mem ds with num and their resp index
        mem = collections.defaultdict(list)
        for i, num in enumerate(nums):
            mem[num].append(i)
        

        for i, num in enumerate(nums):
            if target - num in mem:
                if target - num == num: 
                    if len(mem[num]) > 1:
                        return [i, mem[num][1]]
                else: 
                    return [i, mem[target - num][0]]

        return -1

        
        
        