class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        row,col=len(matrix),len(matrix[0])
        m,res,count_negative=math.inf,0,0
        for i in range(row):
            for j in range(col):
                res+=abs(matrix[i][j])
                m=min(m,abs(matrix[i][j]))
                if matrix[i][j]<0:
                    count_negative+=1
        if count_negative%2==0:
            return res
        out=res-2*m
        return out