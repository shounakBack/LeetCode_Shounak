class Solution:
    def reverse(self, x: int) -> int:
        a=int(str(abs(x))[::-1])
        if a.bit_length()>31:
            return 0
        elif x>0:
            return a
        else:
            return -1*a