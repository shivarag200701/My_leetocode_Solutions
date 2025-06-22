class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        midRow = m // 2
        midColumn = n // 2
        mid = matrix[midRow][midColumn]
        if target <= mid:
            while target < matrix[midRow][0] and midRow >= 0:
                midRow -= 1

            i = 0
            j = n - 1
            mid = (j - i) // 2
            while i <= j:
                if target > matrix[midRow][mid]:
                    i = mid + 1
                    mid = i + (j - i) // 2
                elif target < matrix[midRow][mid]:
                    j = mid - 1
                    mid = i + (j - i) // 2
                else:
                    return True
            return False

        if target >= mid:
            while target > matrix[midRow][n - 1] and midRow < m - 1:
                midRow += 1

            i = 0
            j = n - 1
            mid = (j - i) // 2
            while i <= j:
                if target > matrix[midRow][mid]:
                    i = mid + 1
                    mid = i + (j - i) // 2
                elif target < matrix[midRow][mid]:
                    j = mid - 1
                    mid = i + (j - i) // 2
                else:
                    return True
            return False
