class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        r = 0

        while t <= b:
            r = (b + t)//2
            if target < matrix[r][0]:
                b = r - 1
            elif target > matrix[r][0]:
                if target <= matrix[r][len(matrix[r]) - 1]:
                    break
                else:
                    t = r + 1
            else:
                return True

        row = matrix[r]
        l, r = 0, len(row) - 1

        while l <= r:
            c = (r + l)//2
            if target < row[c]:
                r = c - 1
            elif target > row[c]:
                l = c + 1
            else:
                return True

        return False 