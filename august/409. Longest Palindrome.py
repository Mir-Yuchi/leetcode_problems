import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        for v in collections.Counter(s).values():
            count += v // 2 * 2
            if count % 2 == 0 and v % 2 == 1:
                count += 1
        return count