class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        delta=0
        res=""
        for index,ch in enumerate(s):
            if delta<len(spaces) and index==spaces[delta]:
                res=res+' '+ch
                delta+=1
            else:
                res+=ch
        return res