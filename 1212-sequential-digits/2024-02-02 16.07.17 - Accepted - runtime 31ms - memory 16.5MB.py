class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = "123456789"
        res = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(seq[start: start+length])
                if num >= low and num <= high:
                    res.append(num)
        return res
