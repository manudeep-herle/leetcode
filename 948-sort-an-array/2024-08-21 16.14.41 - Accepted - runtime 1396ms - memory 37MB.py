class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        def merge(l, m, r):
            # Two temporary arrayes
            temp1, temp2 = [], []
            # Merge left and right
            for i in range(l, m+1):
                temp1.append(nums[i])
            for i in range(m+1, r+1):
                temp2.append(nums[i])
            lp, rp, k = 0, 0, l
            while lp < len(temp1) and rp < len(temp2):
                if temp1[lp] < temp2[rp]:
                    nums[k] = temp1[lp]
                    lp += 1
                else:
                    nums[k] = temp2[rp]
                    rp += 1
                k += 1
            
            while lp < len(temp1):
                nums[k] = temp1[lp]
                k += 1
                lp += 1
            while rp < len(temp2):
                nums[k] = temp2[rp]
                k += 1
                rp += 1
        
        def mergeSort(left, right):
            if left >= right: # if len of array is 1
                if left > right:
                    print("l > r", left, right)
                return
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, right)
    
        mergeSort(0, len(nums) - 1)
        return nums
        