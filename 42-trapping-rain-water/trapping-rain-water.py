class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        min_ = 0
        max_ = 0
        area = 0
        max_curr = 0
        for i in range(0,len(height)):
            max_l = max_curr

            # for j in range(i-1,-1,-1):
            #     if height[j] > height[i] and height[j] > max_l and j >= 0:
            #         max_l = height[j]
            max_r = max(height[i:])
            # for j in range(i+1,len(height)):
            #     if height[j] > height[i] and height[j] > max_r:
            #         max_r = height[j]
            if height[i] <= min(max_l,max_r):
                area += min(max_l,max_r) - height[i]
            print(max_l,height[i],max_r,area)
            if height[i] > max_curr:
                max_curr = height[i]
        return area