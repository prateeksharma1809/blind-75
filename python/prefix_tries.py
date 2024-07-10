class Node:
    def __init__(self, val=None):
        self.isEnd = False
        self.neighbours = {}

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in word:
            if i not in curr.neighbours:
                curr.neighbours[i] = Node(i)
            curr = curr.neighbours[i]
        curr.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i in word:
            if i in curr.neighbours:
                curr = curr.neighbours[i]
            else:
                return False
        return curr.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for i in prefix:
            if i in curr.neighbours:
                curr = curr.neighbours[i]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)