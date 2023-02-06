# Link do exercício: https://leetcode.com/problems/convert-the-temperature/submissions/876821438/
class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius+273.15
        fahrenheit = celsius*1.8+32
        return [kelvin, fahrenheit]


assert convertTemperature(36.5) == [309.65,97.7] 
assert convertTemperature(122.11) == [395.26,251.798]