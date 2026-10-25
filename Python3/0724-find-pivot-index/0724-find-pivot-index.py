class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left=0
        suffix_of_1s=total-nums[0]
        if suffix_of_1s==0:
            return 0
   
        for i in range(1,len(nums)):
            left+=nums[i-1]
            right=total-nums[i]-left
            
            if left==right:
                return i

        return -1
            