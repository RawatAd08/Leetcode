class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return 2
        i=0
        j=1
        count=1
        is_valid=True
        while(j<n):
            if nums[i]==nums[j]:
                count+=1
                if count<=2:
                    i+=1
                    nums[i]=nums[j]
                else:
                    is_valid=False
                j+=1
            else:
                if is_valid==False:
                    i+=1
                    nums[i] =nums[j]
                    j+=1
                    count=1
                    is_valid=True
                else:
                    i+=1
                    nums[i]=nums[j]
                    j+=1
                    count=1
        return i+1