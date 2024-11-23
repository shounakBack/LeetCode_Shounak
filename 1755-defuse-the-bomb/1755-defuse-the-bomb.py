class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[]
        for i in range(n):
            s=0
            if k>0:
                for j in range(i+1,i+k+1):
                    ele=code[j%n]
                    s+=ele
                res.append(s)
            elif k<0:
                for j in range(i-abs(k),i):
                    ele=code[(j+n)%n]
                    s+=ele
                res.append(s)
            else:
                res.append(0)
        return res