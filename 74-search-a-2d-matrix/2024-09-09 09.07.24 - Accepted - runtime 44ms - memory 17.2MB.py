class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        def rowSearch(row):
            left, right = 0, COLS - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        # Find the row containing the target
        left, right = 0, ROWS-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                return rowSearch(mid)
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        