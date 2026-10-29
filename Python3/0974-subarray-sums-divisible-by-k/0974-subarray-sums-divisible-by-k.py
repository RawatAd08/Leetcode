class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        n = len(nums)
        prefix = []
        prefix.append(nums[0])

        for i in range(1, n):
            prefix.append(nums[i] + prefix[i-1])

        d = {}
        count = 0

        for j in range(0, n):

            r = prefix[j] % k

            if r == 0:
                count += 1

            if r in d:
                count += d[r]

            d[r] = d.get(r, 0) + 1

        return count