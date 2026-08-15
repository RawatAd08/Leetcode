class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        m=len(ransomNote)
        n=len(magazine)
        if m>n:
            return False

        d1={}
        for key in ransomNote :
            d1[key]=d1.get(key,0)+1

        d2={}
        for key in magazine :
            d2[key]=d2.get(key,0)+1
        
        for key,value in d1.items():
            if key not in d2 or value>d2[key]:
                return False
        return True

