class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
 
        # sort the list in ascending order
        A.sort()
        print(A)
        result = []
        fi = []
        # check if quadruplet is formed by `A[i]`, `A[j]`, and a pair from
        # sublist `A[j+1…n)`
        for i in range(len(A) - 3):
            for j in range(i + 1, len(A) - 2):
                # `k` stores remaining sum
                newTarget = target - (A[i] + A[j])
                # check for sum `k` in sublist `A[j+1…n)`
                low = j + 1
                high = len(A) - 1

                while low < high:
                    if A[low] + A[high] < newTarget:
                        low = low + 1
                    elif A[low] + A[high] > newTarget:
                        high = high - 1
                    # quadruplet with a given sum found
                    elif(True):
                        print((A[i], A[j], A[low], A[high]))
                        if result.count([A[i], A[j], A[low], A[high]]) == 0:
                            result.append([A[i], A[j], A[low], A[high]])
                        (low, high) = (low + 1, high - 1)
        return result
 

        