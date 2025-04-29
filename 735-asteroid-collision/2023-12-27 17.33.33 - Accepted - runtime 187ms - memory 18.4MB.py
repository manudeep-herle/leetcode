class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 1
        while True:
            if i == 0 and len(asteroids) > 1:
                i += 1
            if len(asteroids) <= 1 or i >= len(asteroids):
                print(asteroids, i)
                return asteroids
            if asteroids[i] > 0:
                i += 1
            elif asteroids[i] < 0:
                if asteroids[i-1] > 0:
                    if asteroids[i-1] < abs(asteroids[i]):
                        del asteroids[i-1]
                        i -= 1
                    elif asteroids[i-1] > abs(asteroids[i]):
                        del asteroids[i]
                    else:
                        del asteroids[i]
                        del asteroids[i-1]
                        i -= 1
                else:
                    i += 1

        print(asteroids, i)
        return asteroids
        