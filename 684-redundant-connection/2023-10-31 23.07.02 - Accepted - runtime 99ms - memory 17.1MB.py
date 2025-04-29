class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        temp = set([edges[0][0], edges[0][1]])
        pools = [temp]

        for s,t in edges[1:]:
            print(s, t)
            poolS = None
            poolT = None
            for i in range(len(pools)):
                if s in pools[i]:
                    poolS = i
                if t in pools[i]:
                    poolT = i
            print(poolS, poolT)

            if poolS == None and poolT == None:
                pools.append(set([s, t]))

            if poolS != None and poolT != None and poolS == poolT:
                return [s,t]

            if poolS != None and poolT != None:
                pools[poolS] = pools[poolS].union(pools[poolT])
                pools.pop(poolT)

            else:
                if poolS != None:
                    pools[poolS].add(t)
                    print(pools[poolS])
                elif poolT != None:
                    pools[poolT].add(s)


                
                