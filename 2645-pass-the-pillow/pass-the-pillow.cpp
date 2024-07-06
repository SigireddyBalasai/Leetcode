class Solution {
public:
    int passThePillow(int n, int time) {
        int a = time % (n - 1);
        int b = time / (n - 1);

        if (b % 2 == 0) {
            return 1 + a;
        }
        return n - a;
    }
};