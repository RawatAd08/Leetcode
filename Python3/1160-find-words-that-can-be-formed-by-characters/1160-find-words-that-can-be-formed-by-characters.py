class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        for key in chars:
            d[key]=d.get(key,0)+1
        total_len=0
        d_char={}
        for word in words:
            #dictionary of each word
            for ch in word:
                d_char[ch]=d_char.get(ch,0)+1
            
            #check the frequency of each char 
            good_string=True
            for key,value in d_char.items():
                if key not in d or value>d[key]:
                    good_string=False
                    break
                
            if good_string:
                total_len+=len(word)
            #empty the current dictionary
            d_char={}
                
        return total_len