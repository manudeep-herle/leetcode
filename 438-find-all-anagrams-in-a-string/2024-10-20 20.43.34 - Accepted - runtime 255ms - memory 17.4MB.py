from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        i = len(p) - 1
        countP = Counter(p) 
        countS = Counter(s[0:i+1])
        lenP = len(p)
        res = []
        while True:
            # check if countS and coutP are same
            if "".join(sorted(countS.keys())) == "".join(sorted(countP.keys())):
                flag = True
                for key in countS:
                    if countS[key] != countP[key]:
                        flag = False
                        break
                    
                if flag: 
                    res.append(i+1 - len(p))
                
            countS[s[i-lenP + 1]] -= 1
            if countS[s[i-lenP + 1]] == 0: del countS[s[i-lenP + 1]]
            i += 1
            if i == len(s):
                return res
            countS[s[i]] = countS.get(s[i], 0) + 1
        

