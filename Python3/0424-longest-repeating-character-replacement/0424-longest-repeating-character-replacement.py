class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        i=0
        max_freq=0
        max_len=0
        d={}

        for j in range(n):
            ch=s[j]
            d[ch]=d.get(ch,0)+1#fill the dictonary
            max_freq=max(max_freq,d[ch])
            window_size=j-i+1
            diff=window_size-max_freq
            if diff>k: 
                d[s[i]]-=1#reduce the frequency of ith element
                i+=1 #reduce the window size
            window_size=j-i+1
            max_len=max(max_len,window_size)
        return max_len

