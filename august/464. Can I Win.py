class Solution:
    def helper(self, nums, desiredTotal):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in self.memo:
            return self.memo[key]
        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:],
                               desiredTotal - nums[i]):
                self.memo[key] = True
                return True
        self.memo[key] = False
        return False

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(list(range(1, maxChoosableInteger + 1)),
                           desiredTotal)
