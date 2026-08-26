class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        seen=set()
        repeated=set()

        for  i in range(0,n-10+1):
            new_substring=s[i:i+10]
            #print(new_substring)
            if new_substring not in seen:
                seen.add(new_substring)
            else:
                repeated.add(new_substring)
                
        return list(repeated)
       