class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d=dict()
        for i in range(len(nums)):
            need=target-nums[i]     
            if need in d:
                return [i,d[need]]
            d[nums[i]]=i