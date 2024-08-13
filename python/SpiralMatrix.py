class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        left,top = 0,0
        right, bottom = len(matrix[0]), len(matrix)
        while (left<right and top<bottom ):
            print(left, right, top,bottom)
            for i in range(left, right):
                res.append(matrix[top][i])
            top+=1
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1
            if not (left<right and top<bottom ):
                break
            for i in range(right-1, left,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top,-1):
                res.append(matrix[i][left])
            left+=1
        return res
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))