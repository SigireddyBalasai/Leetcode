class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr= []
        arr.append(s[0])
        for t in range(1,len(s)):
            i = s[t]
            if len(arr) == 0:
                arr.append(i)
                continue
            if i == arr[-1]:
                arr.pop()
            else:
                arr.append(i)
        return "".join(arr)
        
        