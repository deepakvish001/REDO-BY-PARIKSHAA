class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        m = nums
        INF = 10**10
        dp = [INF]*(sum+1)
        dp[0] = 0
        for x in m:
            op = []
            if x <= sum:
                op.append((x,0))
            curr = x
            ops = 0
            while curr*2<=sum:
                curr*=2
                ops+=1
                op.append((curr,ops))
            curr = x
            ops = 0
            while curr // 2>0:
                curr//=2
                ops+=1
                op.append((curr,ops))
            dp1=dp[:]
            rs = [w for w, val in enumerate(dp) if val != INF]
            for val,ct in op:
                for w in rs:
                    w1=w+val
                    if w1>sum:
                        break;
                    if dp[w]+ct<dp1[w1]:
                        dp1[w1]=dp[w]+ct
            dp = dp1
        return dp[sum] if dp[sum] != INF else -1