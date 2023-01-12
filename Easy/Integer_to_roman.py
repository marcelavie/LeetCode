class Solution(object):
    def romanToInt(self, s):
        dict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        atual = 0
        anterior = 0

        for i in range(len(s)):
            atual = dict[s[i]]
            if atual > anterior:
                total = total + atual - 2 * anterior
            else: 
                total += atual

            anterior = atual
        return total
    
    
# Link do exercício: https://leetcode.com/problems/roman-to-integer/description/

