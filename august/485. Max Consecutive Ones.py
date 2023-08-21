class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for i in nums:
            if i:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 0
        return max(ans, cur)