class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        d1_mat = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d1_mat.append(matrix[i][j])

        l = 0
        r = len(d1_mat) - 1

        while l <= r:
            mid = (l + r) // 2

            if d1_mat[mid] == target:
                return True
            elif d1_mat[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
            

