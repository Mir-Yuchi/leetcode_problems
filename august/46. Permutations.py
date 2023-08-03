'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''

from typing import List


class Solution:
    def permute_helper(self, nums, param, result):
        if len(nums) == 0:
            result.append(param)
        for i in range(len(nums)):
            self.permute_helper(nums[:i] + nums[i + 1:], param + [nums[i]], result)

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_helper(nums, [], result)
        return result
