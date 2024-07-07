class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        mod = (time-1)%(n-1)
        div = (time-1)//(n-1)
        if div%2==0:
            return mod+2
        else:
            return n-(mod+1)
        