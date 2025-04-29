class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        
        def recurse(currTotal, num, curr):
            if len(curr) == k and currTotal == n:
                res.add(tuple(curr))
            if currTotal > n or num > 9 or len(curr) > k:
                print(currTotal, num, curr)
                return


            recurse(currTotal, num + 1, curr)
            recurse(currTotal + num, num + 1, curr+[num])
        
        recurse(0,1,[])
        
        return res
        