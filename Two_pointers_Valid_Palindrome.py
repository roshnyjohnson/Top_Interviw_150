class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reverse=""
        s="".join(ch for ch in s if ch.isalnum()).lower()
        for i in range(len(s)-1,-1,-1):
            reverse=reverse+s[i]
        if reverse==s:
            return True
        else:
            return False
        
