class Solution:
    def compressedString(self, word: str) -> str:
        i=0
        res=""
        n=len(word)
        while i<n:
            ch=word[i]
            count=0
            while i<n and ch==word[i]:
                count+=1
                i+=1
            if count<10:
                res=res+str(count)+ch
            else:
                while count>9:
                    res=res+'9'+ch
                    count=count-9
                if count>=0:
                    res=res+str(count)+ch
        return res