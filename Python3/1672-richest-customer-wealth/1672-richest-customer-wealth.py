class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum=0
        for sublist in accounts:
            max_sum=max(max_sum,sum(sublist))
        return max_sum
            