class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int: 
        n=len(nums)  
        nums.sort()
        i=0
        window_sum=0
        max_freq=0
        for j in range(n):
            window_sum+=nums[j]
            exp_sum=nums[j]*(j-i+1)
            diff=exp_sum-window_sum
            if diff>k:
                window_sum-=nums[i]
                i+=1
            else:
                max_freq=max(max_freq,j-i+1)
        
        if max_freq==0:
            return 1
        return max_freq
