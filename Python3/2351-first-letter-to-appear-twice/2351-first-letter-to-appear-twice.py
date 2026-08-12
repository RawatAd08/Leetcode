class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq={}
        for ch in s:
            if ch in freq:
                return ch
            freq[ch]=1

    
