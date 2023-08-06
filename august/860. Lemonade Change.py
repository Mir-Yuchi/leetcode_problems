class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dp = [0] * 21
        dp[0] = 1

        for bill in bills:
            if bill == 5:
                dp[5] += 1
            elif bill == 10:
                if dp[5] > 0:
                    dp[5] -= 1
                    dp[10] += 1
                else:
                    return False
            else:
                if dp[10] > 0 and dp[5] > 0:
                    dp[10] -= 1
                    dp[5] -= 1
                    dp[20] += 1
                elif dp[5] > 2:
                    dp[5] -= 3
                    dp[20] += 1
                else:
                    return False

        return True