class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a, b):
            if str(a) + str(b) > str(b) + str(a):
                return +1
            else:
                return -1

        nums = sorted(nums, key = cmp_to_key(compare), reverse = True)
        print(nums)
        return str(int("".join(map(str,nums))))