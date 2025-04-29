class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        rightFalling, leftFalling = [float('inf')] * len(dominoes), [float('inf')] * len(dominoes)
        distFromPrevRightFalling = distFromPrevLeftFalling = float('inf')
        for i in range(0, len(dominoes)):
            if dominoes[i] == "R":
                distFromPrevRightFalling = 0
            elif dominoes[i] == "L":
                distFromPrevRightFalling = float('inf')
            if dominoes[len(dominoes) - 1 - i] == "R":
                distFromPrevLeftFalling = float('inf')
            elif dominoes[len(dominoes) - 1 - i] == "L":
                distFromPrevLeftFalling = 0

            rightFalling[i] = distFromPrevRightFalling
            leftFalling[len(dominoes) - 1 - i] = distFromPrevLeftFalling
            distFromPrevRightFalling += 1
            distFromPrevLeftFalling += 1
            
        res = []
        for i, (distFromPrevRightFalling, distFromPrevLeftFalling) in enumerate(zip(rightFalling, leftFalling)):
            if distFromPrevRightFalling < distFromPrevLeftFalling:
                res.append("R")
            elif distFromPrevRightFalling > distFromPrevLeftFalling:
                res.append("L")
            else:
                res.append(".")
        return "".join(res)

        