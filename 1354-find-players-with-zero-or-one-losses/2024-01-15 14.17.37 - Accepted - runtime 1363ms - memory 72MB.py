class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        oneLoss, zeroLoss, others = set(), set(), set()
        for [win, los] in matches:
            if win not in others and win not in oneLoss:
                zeroLoss.add(win)
            if los in oneLoss:
                oneLoss.remove(los)
                others.add(los)
            elif los in zeroLoss:
                zeroLoss.remove(los)
                oneLoss.add(los)
            elif los in others:
                continue
            else:
                oneLoss.add(los)

        res = [sorted(list(zeroLoss)), sorted(list(oneLoss))]
        return res
        