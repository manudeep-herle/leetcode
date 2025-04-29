class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurse(i):
            # base case when i is out of bounds
            if i == len(nums):
                return [[]]
            perms = recurse(i + 1)
            ret = []

            for perm in perms:
                # place nums[i] in every location in all the perms
                for j in range(len(perm)):
                    ret.append(perm[0:j] + [nums[i]] + perm[j:])
                ret.append(perm + [nums[i]])  # append at the end
            return ret  # return all perms including nums[i] and ahead to the caller

        return recurse(0)
