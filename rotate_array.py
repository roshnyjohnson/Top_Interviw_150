class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        

        temp1=nums[:n-k]
        temp2=nums[n-k:]
        temp3=temp2+temp1
        for i in range (n):
            nums[i]=temp3[i]

        return nums

        
