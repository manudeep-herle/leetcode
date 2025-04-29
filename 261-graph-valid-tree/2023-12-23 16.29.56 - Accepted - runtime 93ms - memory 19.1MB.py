class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        sets = []
        for [i,j] in edges:
            si = sj = None
            for s in range(len(sets)):
                if i in sets[s]:
                    si = s
                if j in sets[s]:
                    sj = s
            if si == None and sj == None:
                newSet = set([i, j])
                sets.append(newSet)
            elif si == None:
                sets[sj].add(i)
            elif sj == None:
                sets[si].add(j)
            elif si == sj:
                return False
            else:
                sets[si].update(sets[sj])
                del sets[sj]

        return len(sets) == 1 and len(sets[0]) == n