class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = 0
        l = 0
        r = len(matrix[0]) - 1
        column = len(matrix) - 1
        targetr = float('inf')

        while row <= column:
            m = (row + column) // 2
            if matrix[m][0] > target :
                column = m - 1
            elif matrix[m][r] < target:
                row = m + 1
            else:
                targetr = m
                break

        if targetr == float('inf'):
            return False
        
        while l<=r:
            m = (l + r) // 2
            if matrix[targetr][m] > target:
                r = m - 1
            elif matrix[targetr][m] < target:
                l = m + 1
            else:
                return True
        
        return False