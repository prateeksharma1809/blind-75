from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        #Transpose except diagonal
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
        # print(matrix)
        #Mirror it along center column
        for i in range(rows):
            for j in range(cols//2):
                matrix[i][j],matrix[i][cols-j-1] = matrix[i][cols-j-1],matrix[i][j]
