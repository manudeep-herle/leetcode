class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = collections.defaultdict(list)
        for s in strs:
            mem["".join(sorted(s))].append(s)
        
        return list(mem.values())
        