class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump=0
        maxreach=0
        currend=0
        for i in range(len(nums)-1):
            if i>maxreach:
                return False
            maxreach=max(maxreach,nums[i]+i)
            if i==currend:
                jump+=1
                currend=maxreach
        return jump
