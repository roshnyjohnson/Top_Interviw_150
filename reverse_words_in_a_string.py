class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        words=s.split()
        words2=words[::-1]
        s=" ".join(words2)
        return s
        
