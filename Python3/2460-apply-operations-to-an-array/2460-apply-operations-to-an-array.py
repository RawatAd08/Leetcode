class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        i=0
        for j in range(0,len(nums)):
            if nums[j]!=0:
                #swap
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
           
        return nums