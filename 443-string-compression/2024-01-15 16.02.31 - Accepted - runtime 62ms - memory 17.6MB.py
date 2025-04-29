class Solution:
    def compress(self, chars: List[str]) -> int:
        start, cur, curLen = 0, chars[0], 1
        res = []
        for i in range(1, len(chars)):
            if chars[i] != cur:
                if curLen > 1:
                    endIndex = i - 1 - len(str(curLen))
                    while start < endIndex:
                        chars[start] = "del"
                        start += 1
                    for j in range(len(str(curLen))):
                        chars[start + 1 + j] = str(curLen)[j]
                cur = chars[i]
                curLen = 1
                start = i
            else:
                curLen += 1

        if curLen > 1:
            endIndex = len(chars) - 1 - len(str(curLen))
            while start < endIndex:
                chars[start] = "del"
                start += 1
            for j in range(len(str(curLen))):
                chars[start +1+ j] = str(curLen)[j]

        i = 0
        while i < len(chars):
            if chars[i] == "del":
                del chars[i]
            else:
                i += 1

