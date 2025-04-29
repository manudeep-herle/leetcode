class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        freq_sets = list(hmap.items())
        freq_sets.sort(reverse=True, key= lambda item: item[1])

        a = []
        for i in range(0, k):
            a.append(freq_sets[i][0])
        return a
        





