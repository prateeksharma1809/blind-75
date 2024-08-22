
from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        topSort = []
        indegree = [0 for _ in range(numCourses)]
        predict = {}
        for course,pre in prerequisites:
            indegree[course]+=1
            predict[pre] = predict.get(pre,[])
            predict[pre].append(course)
            # predict[pre].append(course)
        print(indegree, predict)
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        print(indegree,q)
        while q:
            course = q.popleft()
            print(course)
            topSort.append(course)
            dep = predict.get(course,[])
            for d in dep:
                indegree[d]-=1
                if indegree[d]==0:
                    q.append(d)
                    

        return len(topSort)==numCourses
        

prerequisites = [[1,0]]
print(Solution().canFinish(2,prerequisites))