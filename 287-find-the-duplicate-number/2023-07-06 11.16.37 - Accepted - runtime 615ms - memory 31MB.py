class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow_ = 0
        while True:
            slow_ = nums[slow_]
            slow = nums[slow]
            if slow == slow_:
                return slow

