class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for ch in s:
            ascii=ord(ch)
            if ascii>=65 and ascii<=90:#check if uppercase
                ascii+=32
                ch=chr(ascii)#converted  back to character
            result+=ch
        return result
