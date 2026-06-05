class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr=sorted(arr)

        d=dict()
        rank=1

        #creating dictionary
        for num in sorted_arr: 
            if num not in d:
                d[num]=rank
                rank+=1 
        return [d[x] for x in arr]
         