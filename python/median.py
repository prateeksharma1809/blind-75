class MedianFinder(object):

    def __init__(self):
        # Initialize an empty list to store numbers in sorted order.
        self.lst = []
        # Initialize the length of the list.
        self.l = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # If the list is empty, simply append the number.
        if self.l <= 0:
            self.lst.append(num)
        else:
            # Binary search to find the correct insertion position.
            l, r = 0, self.l - 1
            while l <= r:
                m = (l + r) // 2
                if self.lst[m] < num:
                    l = m + 1
                else:
                    r = m - 1
            # Insert the number at the found position.
            self.lst.insert(l, num)
        
        # Increment the length of the list.
        self.l += 1

    def findMedian(self):
        """
        :rtype: float
        """
        # If the length of the list is even, return the average of the two middle elements.
        if self.l % 2 == 0:
            m = self.l // 2
            return (self.lst[m] + self.lst[m - 1]) / float(2)
        else:
            # If the length is odd, return the middle element.
            return self.lst[self.l // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
