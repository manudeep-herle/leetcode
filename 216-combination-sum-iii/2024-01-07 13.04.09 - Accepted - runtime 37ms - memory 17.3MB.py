class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        
        def recurse(currTotal, num, curr):
            if len(curr) == k and currTotal == n:
                res.add(tuple(curr))
                return
            if currTotal > n or num > 9 or len(curr) > k:
                return


            for i in range(num+1, 10):
                curr.append(i)
                recurse(currTotal + i, i, curr)
                curr.pop()
        
        recurse(0,0,[])
        
        return res
        