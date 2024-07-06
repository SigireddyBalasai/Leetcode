class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr : List[str]= []
        for i in s:
            if arr and i == arr[-1]:
                arr.pop()
            else:
                arr.append(i)
        return "".join(arr)
        
        