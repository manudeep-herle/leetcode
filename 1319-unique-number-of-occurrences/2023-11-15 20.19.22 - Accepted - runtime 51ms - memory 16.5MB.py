class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = {}
        for num in arr:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1
        
        counts = set()
        for key in mem:
            if mem[key] in counts:
                return False
            counts.add(mem[key])

        return True
        

        