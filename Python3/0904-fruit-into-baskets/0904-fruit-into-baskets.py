class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        d={}
        i=0
        max_len=1
        for j in range(0,n):
            if fruits[j] in d:
                d[fruits[j]]+=1
                max_len=max(max_len,j-i+1)


            else:
                if len(d)<2:
                    d[fruits[j]]=1
                    max_len=max(max_len,j-i+1)
                else:
                    while len(d)>1:
                        #shrink the window
                        d[fruits[i]]-=1
                        if(d[fruits[i]]==0):
                            del(d[fruits[i]])
                        i+=1
                    d[fruits[j]]=1

        return max_len
                