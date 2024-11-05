class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def helper(index,last_char,last_char_count,k):
            if k==-1:
                return math.inf
            if index==n:
                return 0
            delete=helper(index+1,last_char,last_char_count,k-1)
            if s[index]==last_char:
                temp=0
                if last_char_count in seen:
                    temp=1
                not_delete=helper(index+1,last_char,last_char_count+1,k)+temp
            else:
                not_delete=helper(index+1,s[index],1,k)+1
            return min(delete,not_delete)
        n=len(s)
        seen=set()
        seen.add(1)
        seen.add(9)
        seen.add(99)
        return helper(0,"",0,k)