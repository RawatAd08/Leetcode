class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n<k:
            return 0

        window_sum=0
        d={}
        #build the first window of size k
        for i in range(k):
            val=nums[i]
            d[val]=d.get(val,0)+1
            window_sum+=val

        if len(d)==k:
            max_sum=window_sum
        else :
            max_sum=0


        for i in range(k,n):
            new=nums[i]
            noToRemove=nums[i-k]

            #remove the outgoing element
            d[noToRemove]-=1
            if d[noToRemove]==0:
                del(d[noToRemove]) # only delete key when truly gone
            window_sum-=noToRemove

            #adding the incoming element
            d[new]=d.get(new,0)+1
            window_sum+=new

            # window is valid only if every element's frequency is 1
            if len(d)==k:
                max_sum=max(window_sum,max_sum)

        return max_sum
