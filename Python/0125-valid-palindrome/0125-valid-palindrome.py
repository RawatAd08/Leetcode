class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        arr=[]
        #creating the array of alphabets
        for ch in s:
            if ch.isalnum():
                arr.append(ch)
        n=len(arr)
        start=0
        end=n-1
        #checking for palindrome
        while(start<=end):
            if arr[start]!=arr[end]:
                return False
            start+=1
            end-=1
        return True

        