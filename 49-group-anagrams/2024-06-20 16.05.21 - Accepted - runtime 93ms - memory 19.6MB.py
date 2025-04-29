class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}
        for s in strs:
            s_ = str(sorted(s))
            if s_ in mem:
                mem[s_].append(s)
            else:
                mem[s_] = [s]
        return list(mem.values())        
