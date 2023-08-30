class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        max_count = max(count.values())
        max_nums = []
        for key, value in count.items():
            if value == max_count:
                max_nums.append(key)
        min_len = len(nums)
        for max_num in max_nums:
            left = nums.index(max_num)
            right = len(nums) - nums[::-1].index(max_num) - 1
            min_len = min(min_len, right - left + 1)
        return min_len