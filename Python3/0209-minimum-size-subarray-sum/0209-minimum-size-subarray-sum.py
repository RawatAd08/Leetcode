class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        j=0
        sum=0
        min_len=float('inf')

        while(j<n):
            sum+=nums[j]#add the no. to the sum
            #decrease the window size
            while(sum>=target):
                min_len=min(min_len,j-i+1)
                sum-=nums[i]
                i+=1

            j+=1#increase the widow size
        
        if(min_len==float('inf')):
            return 0
        return min_len