class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split()   
        m=len(pattern)
        n=len(arr)
        if m!=n:
            return False

        d={}
        for i in range(m) :
            if pattern[i] not in d:
                #if value already exist
                if arr[i] in d.values():
                    return False
                d[pattern[i]]=arr[i]
                
            else:
                if d[pattern[i]]!=arr[i]:
                    return False
        return True