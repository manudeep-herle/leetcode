class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      tb,rb,bb,lb = 0,len(matrix[0]),len(matrix),-1
      r,c = 0,-1
      res = []
      while True:
        # Move right
        c += 1
        if c < rb:
          while c < rb:
            res.append(matrix[r][c])
            c += 1
          c -= 1
          rb = c
          r += 1
        else:
          return res

      
        # Move down
        if r < bb:
          while r < bb:
            res.append(matrix[r][c])
            r += 1
          r-= 1
          bb = r
        else:
          return res

        # Move left
        c -= 1
        if c > lb:
          while c > lb:
            res.append(matrix[r][c])
            c -= 1
          c += 1
          lb = c
        else:
          return res
        
        # Move up
        r -= 1
        if r > tb:
          while r > tb:
            res.append(matrix[r][c])
            r -= 1
          r += 1
          tb = r
          print(tb)
        else:
          return res

      

        