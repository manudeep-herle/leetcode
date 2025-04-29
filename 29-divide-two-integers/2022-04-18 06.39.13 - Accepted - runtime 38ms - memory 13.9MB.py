class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        c=0
        d=abs(dividend)
        di=abs(divisor)
        while d>=di:
            t=di
            m=1
            while d>=t:
                d-=t
                c+=m
                m+=m
                t+=t
            
            
            
        if (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0):
            c=-c
        
        return min(2147483647,max(-2147483648,c))