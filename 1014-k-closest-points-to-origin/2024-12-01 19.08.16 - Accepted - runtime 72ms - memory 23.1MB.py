class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            distances.append((dist, [x, y]))
        distances = sorted(distances, key = lambda dist: dist[0])
        distances = distances[0:k]
        res = []
        for dist in distances:
            res.append(dist[1])
        
        return res