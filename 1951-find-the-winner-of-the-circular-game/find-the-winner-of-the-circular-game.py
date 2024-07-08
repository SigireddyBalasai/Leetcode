class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        n_arr=range(1,n+1)
        # print(n_arr)
        i=0
        while(len(n_arr) >1):
            # print(len(n_arr),n_arr[(i+k-1)%len(n_arr)])
            i=(i+k-1)%len(n_arr)
            del n_arr[i]
        return n_arr[0]    
            