class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False

        # Dimensions of the board.
        rows, cols = len(board), len(board[0])
        
        # Directions for navigating the neighbours (right, up, left, down).
        neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        
        def dfs(row, col, index):
            # If all characters are matched.
            if index == len(word):
                return True
            
            # Check boundaries and character match.
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            
            # Mark the cell as visited by storing its character and replacing it with a placeholder.
            temp, board[row][col] = board[row][col], '#'
            
            # Explore all neighbours.
            for dr, dc in neighbours:
                if dfs(row + dr, col + dc, index + 1):
                    return True
            
            # Restore the original character.
            board[row][col] = temp
            
            return False
        
        # Iterate through all cells to find starting points.
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
