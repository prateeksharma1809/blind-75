from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        return root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, node, result):
            char = board[i][j]
            if char not in node.children:
                return
            
            node = node.children[char]
            if node.word:
                result.append(node.word)
                node.word = None  # Avoid duplicate entries
            
            board[i][j] = '#'  # Mark the board cell as visited

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != '#':
                    dfs(board, ni, nj, node, result)
            
            board[i][j] = char  # Restore the board cell

            # Optimization: Remove the leaf node to prune the Trie
            if not node.children:
                del node

        root = self.buildTrie(words)
        result = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    dfs(board, i, j, root, result)
        
        return result
