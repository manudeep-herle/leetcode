class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        counts = set()
        currNumCount = 1
        for i in range(1,len(arr)):
            print(arr[i])
            if arr[i] == arr[i-1]:
                currNumCount += 1
                continue

            if currNumCount in counts:
                return False
            
            counts.add(currNumCount)
            currNumCount = 1
        
        return currNumCount not in counts

        