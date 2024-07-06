class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr : List[str]= []
        for i in s:
            if arr and arr[-1]==i:
                arr.pop()
                continue
            else:
                arr.append(i)
        return "".join(arr)
        
        