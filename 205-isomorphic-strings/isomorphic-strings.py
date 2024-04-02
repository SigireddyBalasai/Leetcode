class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        dict2={}
        if len(set(s)) != len(set(t)):
            return False
        for i,j in zip(s,t):
            if i in dict.keys():
                if dict[i]!=j:
                     return False
            elif j in dict2.keys():
                if dict2[j]!=i:
                    return False
                    
            dict[i]=j
            dict2[j]=i
        return True