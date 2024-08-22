from typing import List

class Solution:
    def __init__(self):
        self.neighbours = [(0,1), (1,0), (0,-1), (-1,0)]
        self.rows = 0
        self.cols=0
    def dfs(self, grid, row, col):
        if row<0 or col<0 or row>=self.rows or col >=self.cols or grid[row][col]!='1':
            return 
        else:
            grid[row][col]='2'
            for r, c in self.neighbours:
                self.dfs(grid, row+r, col+c)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        res=0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col]=='1':
                    self.dfs(grid, row, col)
                    res+=1
        return res