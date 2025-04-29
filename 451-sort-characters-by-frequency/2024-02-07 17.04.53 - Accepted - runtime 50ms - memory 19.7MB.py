class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        s.sort()
        # Group common characters together
        grouped = []
        cur = s[0]
        for c in s[1:]:
            if c == cur[0]:
                cur += c
            else:
                grouped.append(cur)
                cur = c
        grouped.append(cur)
        grouped.sort(key = len)
        grouped = reversed(grouped)
        return "".join(grouped)

        
