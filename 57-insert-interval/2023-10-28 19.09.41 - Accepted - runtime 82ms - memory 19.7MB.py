class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
                
        left, right = None, None

        for i in range(len(intervals)):
            ci = intervals[i]
            
            if left == None and newInterval[0] <= ci[1]:
                if newInterval[0] >= ci[0]:
                    newInterval[0] = ci[0]
                left = i-1 # need to check later if this is in bounds
            if right == None and newInterval[1] < ci[1]:
                if newInterval[1] >= ci[0]:
                    newInterval[1] = ci[1]
                    right = i+1
                else:
                    right = i
        print(left, right)
        res = [newInterval]
        if left != None:
            res = intervals[0:left+1] + res 
        if left == None:
            res = intervals + res
        if right != None:
            res = res + intervals[right:]

        return res


                



        