'''
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

    It has a length of k.
    It is a divisor of num.

Given integers num and k, return the k-beauty of num.

Note:

    Leading zeros are allowed.
    0 is not a divisor of any value.

A substring is a contiguous sequence of characters in a string.
'''
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        n = len(num)
        if k > n: return 0
        if k == n: return 1
        ans = 0
        for i in range(n-k+1):
            if num[i] == '0': continue
            if int(num[i:i+k]) % int(num[i]) == 0:
                ans += 1
        return ans