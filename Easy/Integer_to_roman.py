# Link do exercício: https://leetcode.com/problems/roman-to-integer/description/
def romanToInt(s):
    valores = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    anterior = 0

    for romano in s:
        valor_atual = valores[romano]
        if valor_atual > anterior:
            total = total + valor_atual - 2 * anterior
        else: 
            total += valor_atual

        anterior = valor_atual
    return total
    

assert romanToInt('III') == 3
assert romanToInt("LVIII") == 58 
assert romanToInt("MCMXCIV") == 1994
