class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pools = [set([edges[0][0], edges[0][1]])]

        for s,t in edges[1:]:
            poolS = poolT = None

            for i in range(len(pools)):
                if s in pools[i]:
                    poolS = i
                if t in pools[i]:
                    poolT = i

            if poolS == None and poolT == None:
                pools.append(set([s, t]))
                continue

            if poolS == poolT:
                return [s,t]

            if poolS != None and poolT != None:
                pools[poolS] = pools[poolS].union(pools[poolT])
                pools.pop(poolT)

            else:
                if poolS != None:
                    pools[poolS].add(t)
                elif poolT != None:
                    pools[poolT].add(s)


                
                