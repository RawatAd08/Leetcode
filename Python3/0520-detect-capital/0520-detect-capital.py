class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        n=len(word)
        count=0
        if word.islower() or word.isupper():
            return True
        for i in range(n):
            if i==0 and word[i].islower():
                    return False
                
            else:
                if word[i].isupper():
                    count+=1
                    if count==2:
                        return False
        
        return True
                
            