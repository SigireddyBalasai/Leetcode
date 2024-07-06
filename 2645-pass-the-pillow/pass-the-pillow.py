class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # t = 0
        # upgrade = +1
        a = time % (n-1)
        b = time // (n-1)
        if b % 2 == 0:
            return 1+a
        else:
            return n - a
        # for i in range(time+1):
        #     if t == n or (t == 1 and upgrade == -1):
        #         upgrade = -upgrade
        #     t += upgrade
        #     print(t,i)
        # return t
