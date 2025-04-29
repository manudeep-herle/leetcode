class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = {}
        res = []
        stack = []
        for num in nums2:
            if stack and stack[-1] < num:
                while stack and stack[-1] < num:
                    mem[stack[-1]] = num
                    stack.pop()
                stack.append(num)
            else:
                stack.append(num)
        
        while stack:
            mem[stack[-1]] = -1
            stack.pop()
        for num in nums1:
            res.append(mem[num])

        return res

            
        