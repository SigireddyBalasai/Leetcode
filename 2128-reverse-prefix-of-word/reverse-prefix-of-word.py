class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ok = ""
        stack = []
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i] != ch:
                stack.append(word[i])
            else:
                stack.append(word[i])
                break
        for j in stack[::-1]:
            ok += j
        i += 1
        for t in range(i,len(word)):
            ok += word[t]
        print(ok)
        return ok