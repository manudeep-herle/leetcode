from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = Counter(nums)
        freqNum = defaultdict(list)
        for num in numFreq:
            freqNum[numFreq[num]].append(num)
        
        res = []
        for freq in sorted(freqNum.keys(), reverse= True):
            res += freqNum[freq]
            if len(res) == k:
                break
        return res