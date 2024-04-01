class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        for t in digits:
            i = i * 10 + t
        i += 1
        arr = []
        while(i % 10 != 0 or i):
            arr.append(i%10)
            i = i // 10
        return arr[::-1]