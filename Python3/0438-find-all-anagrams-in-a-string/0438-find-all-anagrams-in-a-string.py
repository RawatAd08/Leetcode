class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        window_size=len(p)#window size
        lst=list()
        if window_size>n:
            return lst
        dp={}
        is_anagram=True
        #create the first dictionary of p
        for k in range(0,window_size):
            dp[p[k]]=dp.get(p[k],0)+1
        
        #create the dictonary of first window of s
        i=0
        ds={}
        for j in range(0,window_size):
            ds[s[j]]=ds.get(s[j],0)+1
        
        if dp!=ds:
            is_anagram=False
        else:
            lst.append(i)
        #shift the 1st window
        ds[s[i]]-=1
        if ds[s[i]]==0:
            del(ds[s[i]])
        i+=1
        #check for the remaining windows
        for j in range(window_size,n):
            is_anagram==True
            ds[s[j]]=ds.get(s[j],0)+1

            if dp!=ds:
                is_anagram=False
            else:
                lst.append(i)
            #shift the window
            ds[s[i]]-=1
            if ds[s[i]]==0:
                del(ds[s[i]])
            i+=1

        return lst

