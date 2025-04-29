class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hmap = {}
        for num in hand:
            hmap[num] = hmap.get(num, 0) + 1
        keys = sorted(list(hmap.keys()))
        while len(keys):
            st = keys[0]
            for num in range(st, st + groupSize):
                if num not in hmap:
                    return False
                hmap[num] -= 1
                if hmap[num] == 0:
                    if num != keys[0]:
                        return False
                    keys.pop(0)


        return True