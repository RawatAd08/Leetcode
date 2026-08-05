class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_len=m+n
        i=m
        j=0
        while(i<nums1_len and j<n):
            if (nums1_len>1):
                if(nums2[j]!=0):
                    nums1[i]=nums2[j]
                i+=1
                j+=1
            else:
                if(n!=0):
                    nums1[0]=nums2[0]
                return nums1
        return nums1.sort()
                
                
                
        