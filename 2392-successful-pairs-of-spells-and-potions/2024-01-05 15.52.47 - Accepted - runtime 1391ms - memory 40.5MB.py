class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        def findCount(spell):
            l,r = 0, len(potions)-1
            count = 0
            while l <= r:
                mid = (l+r)//2
                strength = spell * potions[mid]
                if strength == success:
                    count = len(potions)-mid
                    r = mid - 1
                elif strength < success:
                    l = mid + 1
                else:
                    count = len(potions) - mid
                    r = mid - 1
            return count

        for spell in spells:
            count = findCount(spell)
            res.append(count)
        
        return res
        