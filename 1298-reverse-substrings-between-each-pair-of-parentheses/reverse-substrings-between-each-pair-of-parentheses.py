class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if i == ")":
                ar2=[]
                t =stack.pop() 
                while(t != '('):
                    ar2.append(t)
                    t=stack.pop()
                for j in ar2:
                    stack.append(j)
            else:
                stack.append(i)     
        return "".join(stack)           

        