class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int sum=numBottles;
        int num_full=numBottles;
        int num_empty=numBottles;
        while(num_full>0)
        {
            // sum= sum+num_full;
            // num_empty=num_empty+num_full;
            num_full = num_empty/numExchange;
            num_empty=num_empty%numExchange;
            sum= sum+num_full;
            num_empty=num_empty+num_full;
        }
        return sum;
    }
};