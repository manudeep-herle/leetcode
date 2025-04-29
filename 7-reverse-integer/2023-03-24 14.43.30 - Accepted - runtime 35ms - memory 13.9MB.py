class Solution:
    def reverse(self, x: int) -> int:
        ul = 2 ** 31 -1
        ll = - 2 ** 31
        # Convert int to string
        s = str(x)
        neg =  False
        if s[0] == '-':
            neg = True
            s = s[1:]
        # Reverse string
        s = s[::-1]

        a = int(s)
        if neg:
            a = -a
        if a > ul:
            return 0
        if a < ll:
            return 0
        return a


