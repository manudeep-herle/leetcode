from collections import defaultdict 

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hmap = defaultdict(lambda: [0] * len(words))
        res = []
        for i, word in enumerate(words):
            for c in word:
                hmap[c][i] += 1

        for key in hmap.keys():
            val = min(hmap[key])
            for _ in range(val):
                res.append(key) 
            
        return res  