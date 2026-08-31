class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        #build 1st widow
        window_sum=sum(arr[:k])
        avg=window_sum/k
        avg_count=0
        if avg>=threshold:
            avg_count+=1
        
        for i in range(k,n):
            window_sum+=arr[i]
            window_sum-=arr[i-k]
            avg=window_sum/k
            if avg>=threshold:
                avg_count+=1

        return avg_count

        # n=len(arr)
        # i=0
        # avg_count=0
        # for i in range(n-k+1):
        #     window_sum=sum(arr[i:i+k])
        #     avg=window_sum/k
        #     if avg>=threshold:
        #         avg_count+=1
        #     #slide the window
        #     window_sum-=arr[i]
        #     i+=1
        # return avg_count