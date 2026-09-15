class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        start=0
        end=n-1
        pos=letters[0]

        if letters[end]==target:
            return pos

        while(start<=end):
            mid=start-(start-end)//2
            if letters[mid]==target :
                pos=max(pos,target)
                start=mid+1

            elif(letters[mid]<target):
                start=mid+1

            else:
                pos=letters[mid]
                end=mid-1

        return pos