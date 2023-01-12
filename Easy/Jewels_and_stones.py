class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        total = 0
        for i in stones:
            if i in jewels:
                total =total +1
        return total