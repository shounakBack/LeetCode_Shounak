from heapq import *
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def helper(passed,total_students):
            return (passed+1)/(total_students+1)-(passed/total_students)
        q=[]
        for passed,total_students in classes:
            increment=helper(passed,total_students)
            heappush(q,(-increment,passed,total_students))
        for i in range(extraStudents):
            gain,passed,total_students=heappop(q)
            heappush(q,(-helper(passed+1,total_students+1),passed+1,total_students+1))
        res=0
        while q:
            gain,passed,total_students=heappop(q)
            res+=(passed/total_students)
        return res/len(classes)