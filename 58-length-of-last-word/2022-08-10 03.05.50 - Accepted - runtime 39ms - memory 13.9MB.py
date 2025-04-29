class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            if s[i] == " ":
                if res == 0:
                    continue
                else:
                    print(res)
                    return res
            else:
                print("incrementing res")
                res += 1
        return res
                
        