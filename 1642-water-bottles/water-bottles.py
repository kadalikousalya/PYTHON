class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result=numBottles
        empty=numBottles
        while empty>=numExchange:
            full=empty//numExchange
            result+=full
            empty=(empty%numExchange)+full
        return result


        