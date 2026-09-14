class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort()
        i=0
        j=1
        while(j<len(intervals)):
            min_1st=intervals[i][0]
            max_1st=intervals[i][1]
            min_2nd=intervals[j][0]
            max_2nd=intervals[j][1]
            if (min_1st==min_2nd) or max_1st==max_2nd or max_1st>=min_2nd:
                if max_1st>=max_2nd:
                    intervals.pop(j)
                else:
                    intervals[i][1]=intervals[j][1]
                    intervals.pop(j)
            else:
                i+=1
                j+=1

        return intervals
        

        