# 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        pars = {'IV': 4,'IX': 9, 'XL': 40,'XC': 90, 'CD': 400,'CM': 900}
        indv = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}

        coun = 0
        for x,v in pars.items():
            if x in s:
                s = s.replace(x, "")    
                coun += v

        for x in s:
            if x in indv:
                coun += indv[x] 

        return coun

# num = "MCMXCIV"
# print(romanToInt(num))

values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

s = "MCMXCIV"   
total = 0
last_value = 0
print(s)
print(reversed(s))

# Recorremos el string en reversa
for char in reversed(s):
    print(char)
    current_value = values[char]

    if current_value < last_value:
        # Caso como "IV" (1 < 5), restamos 1
        total -= current_value
    else:
        # Caso normal, sumamos
        total += current_value
    
    last_value = current_value

print(total)