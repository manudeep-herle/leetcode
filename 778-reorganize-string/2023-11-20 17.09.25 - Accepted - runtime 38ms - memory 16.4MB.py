from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        # First pass to get count of each character
        count = {}
    
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)
        
        res = ""
        while pq:
            f = heappop(pq)
            if not res or f[1] != res[-1]:
                res += f[1]
                if f[0] + 1 < 0:
                    heappush(pq, (f[0] + 1, f[1]))
            elif pq:
                s = heappop(pq)
                res += s[1]
                if s[0] + 1 < 0:
                    heappush(pq, (s[0] + 1, s[1]))
                heappush(pq, f)
            else:
                return ""             
        return res   

        

                       
        
