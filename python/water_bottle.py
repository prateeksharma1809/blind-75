class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles
        empty = numBottles
        while empty >= numExchange:
            new_filled = empty // numExchange
            empty = empty % numExchange
            result += new_filled
            empty += new_filled
        return result
