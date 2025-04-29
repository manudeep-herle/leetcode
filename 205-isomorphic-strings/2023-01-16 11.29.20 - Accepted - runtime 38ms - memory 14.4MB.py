class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = j = 0
        s = [*s]
        m = {}
        rm = {}
        for i in range(len(s)):
            if s[i] in m:
                s[i] = m[s[i]]
            elif s[i] not in m and t[i] in rm:
                print(s[i],m,t[i],rm)
                return False
            else:
                m[s[i]] = t[i]
                rm[t[i]] = s[i]
                s[i] = t[i]

        s = "".join(s)
        print(s,t)
        if s == t:
            return True
        return False

                
                    


