class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m=len(s)
        n=len(t)
        if m!=n:
            return False

        freq1={}
        for key1 in s:
            freq1[key1]=freq1.get(key1,0)+1

        freq2={}
        for key2 in t:
            freq2[key2]=freq2.get(key2,0)+1

        if freq1==freq2:
            return True
        return False