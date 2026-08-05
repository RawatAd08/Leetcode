class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #remove duplicates
        n=len(nums)
        i=0
        j=1
        while(i<n-1 and j<n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        #find the max and 3rd max
        new_arr=nums[:i+1]
        m=len(new_arr)
        if m<3:
            return new_arr[m-1]
        return new_arr[m-3]