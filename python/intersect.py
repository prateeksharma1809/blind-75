class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        res=[]
        for i in nums1:
            map1[i] = map1.get(i,0)+1
        for i in nums2:
            if i in map1 and map1[i]>0:
                res.append(i)
                map1[i]-=1
        return res