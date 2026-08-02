class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        j=1
        while(i<n-1 and j<n):
            if (nums[i]==0):
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                j+=1
            else:
                i+=1
                j+=1
        return nums