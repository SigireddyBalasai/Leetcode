from math import log2
class Solution:
    def reverse(self, x: int) -> int:
        t = 0
        c = 1
        if x == 0:
            return 0
        if x < 0:
            c = 0
            x = -x
        while(x % 10 != 0 or x):
            #print(x % 10)
            t = t * 10 + x % 10
            x = x // 10
        if c == 0:
            t = -t
        #print(log2(abs(t)),log2(abs(t))>= 31)
        if log2(abs(t)) > 31:
            return 0
        return t 