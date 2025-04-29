class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sColor = image[sr][sc]
        visited = set()

        def colorCell(r, c):
            if r < 0 or c < 0 or r == len(image) or c == len(image[0]) or (r,c) in visited or image[r][c] != sColor:
                return
            else:
                image[r][c] = color
                visited.add((r,c))
                colorCell(r+1, c)
                colorCell(r, c+1)
                colorCell(r-1, c)
                colorCell(r, c-1)
        colorCell(sr, sc)
        return image
