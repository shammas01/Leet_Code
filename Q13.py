class Solution:
    def romanToInt(self, roman_input: str) -> int:
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000 }
        number=0
        for i in range(len(roman_input)-1):
            print(roman[roman_input[i]])
            if roman[roman_input[i]] < roman[roman_input[(i+1)]]:   #
                number-=roman[roman_input[i]]     # n=57
            else:
                number+=roman[roman_input[i]]
        return number+roman[roman_input[-1]]
