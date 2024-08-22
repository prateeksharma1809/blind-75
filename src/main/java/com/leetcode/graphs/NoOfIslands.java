package com.leetcode.graphs;

public class NoOfIslands {
    private void dfs(char[][] grid,int  row,int  col){

        if(grid[row][col]!='1'){
            return;
        }
        grid[row][col]='2';
        if(row+1<grid.length && grid[row+1][col]=='1'){
            dfs(grid, row+1, col);
        }
        if(row-1>=0 && grid[row-1][col]=='1'){
            dfs(grid, row-1, col);
        }
        if(col+1<grid[0].length && grid[row][col+1]=='1'){
            dfs(grid,row, col+1);
        }
        if(col-1>=0 && grid[row][col-1]=='1'){
            dfs(grid, row,col-1);
        }

    }
    public int numIslands(char[][] grid) {
        int res=0;
        for(int row=0; row<grid.length;row++){
            for(int col=0; col<grid[0].length;col++){
                if (grid[row][col]=='1'){
                    this.dfs(grid, row,col);
                    res++;
                }
            }
        }
        return res;
    }
}
