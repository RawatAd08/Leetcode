class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n   #reduce the value of k is k>n
        nums.reverse()#reverse the array
        nums[:k]=reversed(nums[:k])#reverse the 1st k element
        nums[k:]=reversed(nums[k:])#reverse the remaining
        return nums