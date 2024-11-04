class Solution:
    def compress(self, chars: List[str]) -> int:
        i,index,final_index=0,0,0
        while index<len(chars):
            ch=chars[index]
            count=0
            i=index
            while i<len(chars) and ch==chars[i]:
                i+=1
                count+=1
            if count==1:
                chars[final_index]=ch
                final_index+=1
            elif count<=9:
                chars[final_index]=ch
                final_index+=1
                chars[final_index]=str(count)
                final_index+=1
            else:
                temp=str(count)
                chars[final_index]=ch
                final_index+=1
                for ch1 in temp:
                    chars[final_index]=ch1
                    final_index+=1
            index=i
        return final_index