class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        x = [[] for _ in range(n)]
        for i in range(1,n):
            x[parent[i]].append(i)

        y = (parent, nums)
        d = [0] * n
        d[0] = 1
        q = [0]
        for u in q:
            for v in x[u]:
                d[v] = d[u] + 1
                q.append(v)
        h = d[q[-1]]
        ans = 0
        for i in range(n):
            ans += nums[i] * (h - d[i]+1)
        return ans