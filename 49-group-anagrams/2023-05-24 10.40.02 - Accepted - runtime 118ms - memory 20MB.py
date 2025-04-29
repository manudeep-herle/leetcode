class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort the list and words within
        og = strs[:]
        hmap = {}
        for i in range(0, len(strs)):
            strs[i] = ''.join(sorted(strs[i]))
            if strs[i] not in hmap:
                hmap[strs[i]] = []
            hmap[strs[i]].append(og[i])

        ans = []
        for key in hmap:
            ans.append(hmap[key])

        return ans
