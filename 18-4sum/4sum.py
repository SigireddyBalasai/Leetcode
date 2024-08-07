class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        res = set()
        for i in range(n):
            for j in range(i+1,n):
                k = j+1
                l = n-1
                while k<l:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum == target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        res.add(tuple(temp))
                        k += 1
                        l -= 1
                    elif sum<target:
                        k += 1
                    elif sum>target:
                        l -= 1
        ans = list(res)
        return ans
                    
                
                
                