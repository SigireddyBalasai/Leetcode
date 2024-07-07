import math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum=0
        num_full=numBottles
        num_empty=0
        while(num_full>0):
            sum+=num_full
            num_empty+=num_full
            num_change = math.floor(num_empty/numExchange)
            num_full=num_change
            num_empty-=num_change*numExchange
        return sum
        