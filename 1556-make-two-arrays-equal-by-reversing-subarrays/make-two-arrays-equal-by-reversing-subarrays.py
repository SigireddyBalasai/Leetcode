class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        if sum(target)!=sum(arr):
            return False    
        dict_ = {}    
        for i in range(len(arr)):
            if arr[i] in dict_:
                dict_[arr[i]] += 1
            else:
                 dict_[arr[i]] = 1
            if target[i] in dict_:
                dict_[target[i]] -= 1
            else:
                 dict_[target[i]] = -1
        for i in dict_:
            if dict_[i] != 0:
                return False
        return True        

                     

        