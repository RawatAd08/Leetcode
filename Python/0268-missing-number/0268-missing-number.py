class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        expected_sum=0
        for i in range(0,n+1):
            expected_sum+=i

        received_sum=0
        for num in nums:
            received_sum+=num
        return expected_sum-received_sum
         