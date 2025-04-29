from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        minH = list(counts.keys())
        heapify(minH)
        pushbackQ = []

        while len(minH) >= groupSize:
            prev = None
            for _ in range(groupSize):
                card = heappop(minH)
                # Check if the card is 1 bigger than prev card
                if prev != None and card != prev+1:
                    return False
                prev = card
                # Decrement the count of card from counts var
                counts[card] -= 1
                if counts[card] != 0:
                    pushbackQ.append(card)
            # Push cards with non zero counts back to minH
            while pushbackQ:
                heappush(minH, pushbackQ.pop())
        
        return True if not minH else False

                