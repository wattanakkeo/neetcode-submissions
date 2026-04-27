class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while (top <= bottom):
            midRow = (top + bottom) // 2
            if (target < matrix[midRow][0]):
                bottom = midRow - 1
            elif (target > matrix[midRow][COLUMNS - 1]):
                top = midRow + 1
            else:
                break
        
        if not (top <= bottom):
            return False

        l, r = 0, COLUMNS - 1
        while (l <= r):
            mid = (l + r) // 2
            if (target < matrix[midRow][mid]):
                r = mid - 1
            elif (target > matrix[midRow][mid]):
                l = mid + 1
            else:
                return True
        return False
        
