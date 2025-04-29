class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        pos = [i for i in range(len(deck))]
        pos = deque(pos)
        deck.sort()
        res = [0] * len(deck)
        i = 0

        while len(pos) > 1:
            cur = pos.popleft()
            send = pos.popleft()
            pos.append(send)
            res[cur] = deck[i]
            i += 1

        if pos:
            res[pos[0]] = deck[i]

        return res            


        
        