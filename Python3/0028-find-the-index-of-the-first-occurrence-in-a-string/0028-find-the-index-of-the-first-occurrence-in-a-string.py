class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(haystack)
        n=len(needle)
        if m<n:
            return -1

        i=0
        j=0
        while(i<m and j<n):
            if needle[j]==haystack[i]:
                i+=1
                j+=1
            else:
                i=i-j+1
                j=0
        if j>n-1:
            return i-j
        return -1
        