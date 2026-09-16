class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        start=0
        end=n-1

        while(start<=end):
            mid=start-(start-end)//2
            if letters[mid]>target:
                end=mid-1
            else:
                start=mid+1
        
        if start==n:
            return letters[0]

        return letters[start]