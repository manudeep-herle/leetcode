class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(10)]
        cols  = [{} for _ in range(10)]
        miniboxes = [{} for _ in range(10)]

        # Traverse board in row major order.
        row = 0
        for r in board:
            col = 0

            for num in r:
                if num == ".":
                    col += 1
                    continue
                # Check if number already in row
                if num in rows[row]:
                    return False
                rows[row][num] = True
                # Check if number already in col
                if num in cols[col]:
                    return False
                cols[col][num] = True
                # Check if number already in minibox
                mb = int(col / 3) + (3 * int(row / 3)) 
                if num in miniboxes[mb]:
                    return False
                miniboxes[mb][num] = True
                
                col += 1
            row += 1
        return True            
