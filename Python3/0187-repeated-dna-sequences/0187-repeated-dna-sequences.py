class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        substring=s[:10]#build 1st window

        d={}
        d[substring]=1
        print(substring)
        ans=[]
        for  i in range(10,n):
            new_substring=s[i-10+1:i+1]
            #print(new_substring)
            if new_substring not in d:
                d[new_substring]=1
            else:
                if new_substring not in ans:
                    ans.append(new_substring)
                

        return ans
       