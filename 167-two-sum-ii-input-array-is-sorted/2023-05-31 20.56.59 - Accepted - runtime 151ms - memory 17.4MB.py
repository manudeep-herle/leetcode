class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            summ = numbers[lp] + numbers[rp]
            if summ == target:
                return [lp+1, rp+1]
            elif summ < target:
                lp += 1
            elif summ > target:
                rp -= 1

            
