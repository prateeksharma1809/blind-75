class Node:
    def __init__(self, neighbours={}):
        self.neighbours=neighbours
        self.isEnd=False
    
class WordDictionary(object):

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.neighbours:
                newNode = Node()
                node.neighbours[char] = newNode
                node = newNode
            else:
                node = node.neighbours[char]
        node.isEnd=True
        # print(self.root)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dotSearch(st, curr):
            # print(type(curr), st, curr.isEnd)
            if len(st)<=0 and curr.isEnd:
                return True
            if len(st)<=0:
                return False
            res = False
            if st[0]=='.':
                for _,value in curr.neighbours.items():
                    res = res or dotSearch(st[1:], value)
                return res
            elif st[0] in curr.neighbours:
                return dotSearch(st[1:], curr.neighbours[st[0]])
            else:
                return False
        return dotSearch(word, self.root )

# # Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# # obj.addWord('bad')
# print( obj.search('a'))