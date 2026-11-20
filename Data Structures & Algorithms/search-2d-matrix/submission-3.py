class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sorted arr and search = binary search
        # run binary search on rows to find out which row contains the target
        # validate the first binary search to ensure it is not invalid
        # run binary search on that individual row to find out the target
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        while (top <= bottom):
            row = top + ((bottom - top) // 2)
            if (target > matrix[row][-1]):
                top = row + 1
            elif (target < matrix[row][0]):
                bottom = row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        row = top + ((bottom - top) // 2)
        l, r = 0, cols - 1
        while (l <= r):
            mid = l + ((r - l) // 2)
            if (target > matrix[row][mid]):
                l = mid + 1
            elif (target < matrix[row][mid]):
                r = mid - 1
            else:
                return True
        
        return False


