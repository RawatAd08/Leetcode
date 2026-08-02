class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        #count frequency
        for key in nums:
            freq[key]=freq.get(key,0)+1
        #if any vlaue of key>1,contain duplicate
        for key in freq:
            if freq.get(key)>1:
                return True
        return False
        