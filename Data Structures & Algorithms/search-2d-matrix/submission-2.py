class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        t, b = 0, rows - 1
        l, r = 0, cols - 1

        while t <= b:
            row = (b + t)//2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break

        if t > b:
            return False

        row = (t + b)//2
        while l <= r:
            m = (r + l)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
        return False