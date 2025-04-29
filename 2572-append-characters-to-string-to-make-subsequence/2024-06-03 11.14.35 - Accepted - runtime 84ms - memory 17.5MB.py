class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = tp = 0
        count = 0
        while tp < len(t):
            if sp >= len(s):
                return len(t) - count
            if s[sp] == t[tp]:
                count += 1
                tp += 1
            sp += 1

        return len(t) - count
            

        