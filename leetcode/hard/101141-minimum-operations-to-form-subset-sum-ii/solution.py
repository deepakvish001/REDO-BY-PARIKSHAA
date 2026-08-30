import collections
class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        z = nums
        sv = sum
        INF = 10**10
        dp = [INF] * (sv+1)
        dp[0] = 0
        for num in z:
            d = {num: 0}
            q = collections.deque([num])
            while q:
                curr = q.popleft()
                d1 = d[curr]
                nxt1=curr*2
                if nxt1<=sv and nxt1 not in d:
                    d[nxt1] = d1+1
                    q.append(nxt1)
                nxt2=curr//2
                if nxt2 not in d:
                    d[nxt2]=d1+1
                    q.append(nxt2)
            op = []
            for val, ops in d.items():
                if 0 < val <= sv:
                    op.append((val,ops))
            dp1 = dp[:]
            rs = [w for w in range(sv+1) if dp[w]!=INF]
            for val, ops in op:
                for w in rs:
                    nxt = w + val
                    if nxt <= sv:
                        cand = dp[w] + ops
                        if cand < dp1[nxt]:
                            dp1[nxt] = cand
            dp = dp1
        return dp[sv] if dp[sv] != INF else -1