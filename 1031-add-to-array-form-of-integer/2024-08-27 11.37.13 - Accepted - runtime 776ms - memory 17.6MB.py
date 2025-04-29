class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_form = 0
        multiplier = 1
        for digit in reversed(num):
            num_form += multiplier * digit
            multiplier *= 10
        num_form += k

        res = []
        while num_form:
            res.append(num_form % 10)
            num_form = num_form // 10
        return reversed(res)

        