class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink=numBottles
        empty=numBottles
        while empty>=numExchange:
            empty=empty-numExchange
            numExchange+=1
            drink+=1
            empty+=1
        return drink


        