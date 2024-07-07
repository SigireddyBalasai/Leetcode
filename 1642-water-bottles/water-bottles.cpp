class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int sum=0;
        int num_full=numBottles;
        int num_empty=0;
        while(num_full>0)
        {
            sum= sum+num_full;
            num_empty=num_empty+num_full;
            num_full = num_empty/numExchange;
            num_empty=num_empty%numExchange;
        }
        return sum;
    }
};