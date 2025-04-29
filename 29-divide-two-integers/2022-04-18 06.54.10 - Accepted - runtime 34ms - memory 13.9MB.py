class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        c=0
        a_dividend=abs(dividend)
        a_divisor=abs(divisor)
        while a_dividend>=a_divisor:
            curr_divisor=a_divisor
            m=1
            while a_dividend>=curr_divisor:
                a_dividend-=curr_divisor
                c+=m
                m+=m
                curr_divisor+=curr_divisor
            
            
            
        if (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0):
            c=-c
        
        return min(2147483647,max(-2147483648,c))