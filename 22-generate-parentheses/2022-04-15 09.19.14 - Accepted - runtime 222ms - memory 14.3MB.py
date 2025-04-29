class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(A = []):
            if len(A) == n*2:
                print(A)
                if valid(A):
                    # print('valid', A)
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        
        def valid(A):
            bal = 0
            for c in A:
                    if c == '(': bal += 1
                    else: bal -= 1
                    if bal < 0: return False
            return bal == 0
            
                
        generate([])
        return ans
        