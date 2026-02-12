class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        candidate=None
        count=0
        for i in range (n):

            if count==0:
                candidate=nums[i]
            
            if nums[i]==candidate:
                count=count+1

            else:
                count=count-1
        return candidate

