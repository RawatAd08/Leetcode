class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            n=str(num)
            if len(n)%2==0:
                ans+=1
        return ans
