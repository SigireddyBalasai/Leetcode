class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = 0
        upgrade = +1
        if time < n:
            return time + 1
        print(time % (n-1),time // (n-1))
        if (time // (n-1)) == 1:
            return n - time // (n-1) - time % (n-1) + 1
        # print((time+1)%n,(time+1)//n)
        for i in range(time+1):
            if t == n or (t == 1 and upgrade == -1):
                upgrade = -upgrade
            t += upgrade
            print(t,i)
        return t
