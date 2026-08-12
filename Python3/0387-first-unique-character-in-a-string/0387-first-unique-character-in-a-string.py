class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        n=len(s)
        for  key in s:
            d[key]=d.get(key,0)+1

        for key in d:
            if d[key]==1:
                return s.index(key)
        
        return -1