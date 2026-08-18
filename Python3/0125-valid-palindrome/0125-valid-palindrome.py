class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        temp=""
        for ch in s:
            if ch.isalnum():
                temp+=ch
                
        new_str=temp.lower()

        start=0
        end=len(new_str)-1
        while(start<=end):
            if new_str[start]!=new_str[end]:
                return False
            start+=1
            end-=1
        
        return True
