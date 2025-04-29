class Solution:
    def totalMoney(self, n: int) -> int:
      days = n%7
      weeks = n//7
      res = 28 * weeks
      for week in range(1, weeks):
        res += week * 7

      for day in range(1, days+1):
        res += day+weeks

      return res
      
        