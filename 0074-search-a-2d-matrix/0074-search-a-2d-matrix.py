class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])
        l, r = 0, rows - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        if r < 0:
            return False

        s, e = 0, col - 1
        while s <= e:
            mid = (s + e) // 2

            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return False
