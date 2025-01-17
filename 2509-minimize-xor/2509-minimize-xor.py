class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res=0
        set_bit=bin(num2).count('1')
        print(set_bit)
        for i in range(31,-1,-1):
            if set_bit==0:
                break
            if num1 & (1<<i):
                res|=(1<<i)
                set_bit-=1
        for i in range(32):
            if set_bit==0:
                break
            if not (res & (1<<i)):
                res|=(1<<i)
                set_bit-=1
        return res