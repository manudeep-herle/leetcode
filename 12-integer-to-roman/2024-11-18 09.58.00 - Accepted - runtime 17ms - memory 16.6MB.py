class Solution:

    def intToRoman(self, num: int) -> str:
        # Floor number at each decimal place - components
        components = []
        for i, digit in enumerate(str(num)):
            components.append(digit + "0" * (len(str(num)) - i - 1))

        def getRoman(number):
            roman = {1: "I", 5: "V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
            return roman[int(number)]

        res = ""
        # For each component find the roman rep and add them at the end
        for comp in components:
            # Check if a number begins with 4 or 9 - we do 5-1 or 10-1 to rep it
            if comp[0] == '4':
                res += getRoman('1' + '0' * (len(comp) - 1)) + getRoman('5' + '0' * (len(comp) - 1))
                
            elif comp[0] == '9':
                res += getRoman('1' + '0' * (len(comp) - 1)) + getRoman('1' + '0' * len(comp))
            # Else does it begin with 5?
            elif comp[0] == '5':
                res += getRoman(comp)
            # Else it we use 10, 100, 1000 to rep it
            else:
                if comp[0] < '4':
                    res += getRoman('1' + '0' * (len(comp) - 1)) * int(comp[0])
                else:
                    a = getRoman('5' + '0' * (len(comp) - 1)) 
                    b = getRoman('1' + '0' * (len(comp) - 1)) * (int(comp[0]) - 5)

                    res = res + (a+b)
        return res
            
        

        
        # Concat all roman rep of components to get the complete roman numeral
        