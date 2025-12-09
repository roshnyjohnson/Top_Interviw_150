class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reverse=""
        s="".join(ch for ch in s if ch.isalnum()).lower()
        left,right=0,len(s)-1
        while left<right:
            if s[right]!=s[left]:
                return False
            right-=1
            left+=1
        return True
        
