class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1 if s[-1] != "0" else 0
        
        dp = [0] * n
        dp[n - 1] = 1 if s[-1] != "0" else 0
        if s[-2] == "0":
            dp[n - 2] = 0
        elif int(s[n - 2:]) <= 26:
            dp[n - 2] = 1 + dp[n - 1]
        else:
            dp[n - 2] = 1

        for i in range(n - 3, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] + dp[i + 2] if int(s[i:i+2]) <= 26 else dp[i + 1]
        
        return dp[0]