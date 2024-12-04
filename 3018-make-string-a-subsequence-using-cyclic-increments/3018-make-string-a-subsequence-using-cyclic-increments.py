class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index1,index2=0,0
        n1,n2=len(str1),len(str2)
        while index1<n1:
            if index2<n2 and (str1[index1]==str2[index2] or (ord(str1[index1])+1==ord(str2[index2])) or (ord(str1[index1])-25==ord(str2[index2]))):
                index2+=1
            index1+=1
        return index2==n2