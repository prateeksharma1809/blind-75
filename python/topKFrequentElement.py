from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap ={}
        frequency = [[] for _ in range(len(nums)+1)]
        for i in nums:
            countMap[i]=1+countMap.get(i,0)
        for key, value in countMap.items():
            frequency[value].append(key)
        count=0
        result=[]
        for index in range(len(frequency)-1, 0,-1):
            value = frequency[index]
            if(count<k and len(value)!=0):
                for i in value:
                    if(count<k):
                        result.append(i)
                        count+=1
        return result          

        

        

            