class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col =set()
        rows = len(matrix)
        cols=len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        for c in col:
            for r in range(rows):
                matrix[r][c]=0
        for r in row:
            for c in range(cols):
                matrix[r][c]=0