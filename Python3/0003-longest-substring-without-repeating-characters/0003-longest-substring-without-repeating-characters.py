class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        if n==1:
            return 1
        
        result_set=set()
        i=0
        j=0
        for j in range(n):
            if s[j] in result_set:#build the first window
                break
            result_set.add(s[j])
        max_len=len(result_set)
        
        while j<n:
            if s[j] in result_set: 
                result_set.remove(s[i])#shrink window
                i+=1
            else:
                result_set.add(s[j]) #expand window
                max_len=max(max_len,j-i+1)
                j+=1

        return max_len