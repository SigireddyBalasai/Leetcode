class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0
        for i in s:
            if i == "(":
                count += 1
                if count > max_count:
                    max_count = count
            elif(i == ")"):
                count -=1
        return max_count

        