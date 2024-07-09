class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        sum = 0.0
        time = customers[0][0]
        count=0
        for i in customers:
            time=max(i[0],time)
            time += i[1]
            ok = time-i[0]
            # print(ok,time,i)
            sum += ok
            count+=1
        # print(len(customers),sum)
        return (sum/count)