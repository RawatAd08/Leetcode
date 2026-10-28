class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        n=len(nums)
        prefix=list()
        prefix.append(nums[0])

        #Step1: create prefix sum array
        
        for i in  range(1,n):

            prefix.append(nums[i]+prefix[i-1])
            
        #Step2: create a dictionary to store prefix:frequency

        d=dict()
        count=0

        for j in range(0,n):
            if prefix[j]==k:
                count+=1
                
            val=prefix[j]-k
    
            if val in d:
                count+=d[val] #add the value
                
            d[prefix[j]]=d.get(prefix[j],0)+1

        print(d)       
        return count