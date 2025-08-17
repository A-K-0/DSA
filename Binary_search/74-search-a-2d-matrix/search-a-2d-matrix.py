class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1 

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]  

            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
