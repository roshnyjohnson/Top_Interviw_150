class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=0
        for number in nums:
            if pos<2 or number!=nums[pos-2]:
                nums[pos]=number
                pos+=1
        return pos
        del nums[pos:]
        
