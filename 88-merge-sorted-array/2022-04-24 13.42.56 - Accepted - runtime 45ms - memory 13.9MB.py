class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        while i<m and j<n:
            if nums2[j]< nums1[i]:
                nums1.insert(i,nums2[j])
                j += 1
                m += 1
            i += 1
            
        # Trailing zeros in first array   
        i = m
        while i < len(nums1):
            if nums1[i] == 0:
                nums1.pop(i)
            else: i += 1
        
        # Left over elements in second array
        if j<n:
            nums1.extend(nums2[j:n])
        
            