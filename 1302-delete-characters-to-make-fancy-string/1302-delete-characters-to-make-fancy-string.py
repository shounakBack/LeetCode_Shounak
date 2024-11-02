class Solution:
    def makeFancyString(self, s: str) -> str:
        count=1
        prev=s[0]
        out=""
        for ch in s[1:]:
            if ch==prev:
                count+=1
            else:
                if count<3:
                    out+=prev*(count)
                else:
                    out+=prev*2
                prev=ch
                count=1
        if count<3:
            out+=prev*(count)
        else:
            out+=prev*2
        return out