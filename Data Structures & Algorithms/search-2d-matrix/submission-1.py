class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left, right = 0, (row * col) - 1

        while left <= right:
            current = right + left // 2

            row = current // len(matrix[0])
            col = current % len(matrix[0])

            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                right = current - 1
            else:
                left = current + 1
        
        return False
