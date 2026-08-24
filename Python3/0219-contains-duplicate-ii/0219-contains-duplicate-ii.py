class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        d={}
        for i in range(min(k+1, n)):          # <-- CHANGED: prevent IndexError when n < k+1
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                prev_idx=d.get(nums[i])
                if abs(i-prev_idx)<=k:
                    return True
    
        for i in range(min(k+1, n),n):        # <-- CHANGED: match the same bound as above
            left=nums[i-k-1]
            new=nums[i]
            #remove element
            del(d[left])
            
            if new in d:
                prev_idx=d.get(new)
                if abs(i-prev_idx)<=k:
                    return True
                d[new]=i                       # <-- ADDED: refresh stale index when NOT returning True
            else: #add element
                d[new]=i

            
        return False