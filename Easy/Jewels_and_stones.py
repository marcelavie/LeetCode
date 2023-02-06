class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        total = 0
        for stone in stones:
            if stone in jewels:
                total += 1
        return total
# Link do exercício: https://leetcode.com/problems/jewels-and-stones/