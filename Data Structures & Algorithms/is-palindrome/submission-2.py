class Solution:
    def isNotValid(self, ch):
        if ch not in "abcdefghijklmnopqrstuvwxyz0123456789":
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        s = s.lower()
        while(i < j):
            while(i < len(s) and self.isNotValid(s[i])):
                i += 1
            while(j > -1 and self.isNotValid(s[j])):
                j -= 1
            if i >= len(s) or j < 0:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1


        return True 
        