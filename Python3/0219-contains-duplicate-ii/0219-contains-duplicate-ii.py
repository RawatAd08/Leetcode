class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = {}
        for i in range(min(k+1, n)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                prev_idx = d.get(nums[i])
                if abs(i - prev_idx) <= k:
                    return True

        for i in range(k+1, n):          # <-- fixed range
            left = nums[i-k-1]
            new = nums[i]
            del d[left]                  # remove element leaving the window

            if new in d:
                prev_idx = d.get(new)
                if abs(i - prev_idx) <= k:
                    return True
            else:
                d[new] = i

        return False