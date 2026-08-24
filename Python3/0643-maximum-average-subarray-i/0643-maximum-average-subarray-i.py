class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum=sum(nums[:k])#build the first window
        max_avg=window_sum/k

        for i in range(k,n):
            window_sum+=nums[i]#expand the window
            window_sum-=nums[i-k]#shrink the window
            avg=window_sum/k
            max_avg=max(max_avg,avg)

        return max_avg