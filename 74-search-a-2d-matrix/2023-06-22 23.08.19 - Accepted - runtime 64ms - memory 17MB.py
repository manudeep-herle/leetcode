class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up,down = 0, len(matrix) -1


        while up <= down:
            midRow = int((up+down)/2)
            left, right = 0 , len(matrix[0]) - 1
            
            while left <= right:
                mid = int((left+right)/2)

                if matrix[midRow][mid] == target:
                    return True
                elif matrix[midRow][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if matrix[midRow][mid] < target:
                up = midRow + 1
            else: 
                down = midRow - 1

        return False