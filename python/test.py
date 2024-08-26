class Solution(object):
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = []
        for i in range(1,rowIndex+1):
            row = [1 for _ in range(i)]
            if i>=3:
                #logic to pick the previous row and then add the numbers 
                for j in range(1,i-1):
                    row[j] = prev_row[j-1]+prev_row[j]
            prev_row=list(row)
        return prev_row
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res =[]
        for i in range(1,numRows+1):
            row = [1 for _ in range(i)]
            if i>=3:
                #logic to pick the previous row and then add the numbers 
                for j in range(1,i-1):
                    row[j] = res[-1][j-1]+res[-1][j]
            res.append(row)
        return res

print(Solution().getRow(1))