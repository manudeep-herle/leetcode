class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        for triplet in triplets:
            present = []
            for i in range(3):
                if triplet[i] > target[i]:
                    present = []
                    break
                if triplet[i] == target[i]:
                    present.append(i)
            
            for i in present:
                res[i] = True

        return res[0] and res[1] and res[2]
            
        