class Solution:
    def reverse(self, x: int) -> int:
        sign= 1 if x>0 else -1
        x=abs(x)
        li= list(map(int,str(x)))
        li=li[::-1]
        st=int(''.join(map(str,li)))*sign
        if -2**31<st<2**31:
            return st
        else:
            return 0
        