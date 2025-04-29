class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []

        if len(s)>10:
            mem = collections.defaultdict(int)
            curStr = s[0:10]
            mem[curStr] += 1
            for i in range(10, len(s)):
                curStr = curStr[1:] + s[i]
                mem[curStr] += 1
            
            for key in mem:
                if mem[key] > 1:
                    res.append(key)
        
        return res
