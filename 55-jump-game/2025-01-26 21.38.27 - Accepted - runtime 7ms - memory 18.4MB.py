class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # go from back to front
        # minJump = 1 initially, each time a number < minJump is encountered, increment minJump
        # reset minJump to 1 when we reach a number >= minJUmp
        minJump = 1
        nums = nums[0: -1]
        for jump in reversed(nums):
            if jump < minJump:
                minJump += 1
            else:
                minJump = 1
        return minJump == 1

