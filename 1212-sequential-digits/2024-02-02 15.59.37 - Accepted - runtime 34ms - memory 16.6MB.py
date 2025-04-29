class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = "0123456789"
        res = [low]
        curNoDigits, curStartDigit = len(str(low)), 1
        if low > int(seq):
            return []
        # Find the next biggest for start
        prev = "1234533"
        num = None
        while True:
            prev = num
            num = int(seq[curStartDigit: curStartDigit + curNoDigits])

            # We've found all the needed numbers
            if num > high:
                return res[1:]
            elif num >= res[-1]:
                res.append(num)
                if num == 123456789:
                    return res[1:]
            curStartDigit += 1
            if curStartDigit + curNoDigits > 10:
                curStartDigit = 1
                curNoDigits += 1