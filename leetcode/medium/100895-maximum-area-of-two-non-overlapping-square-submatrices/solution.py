class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        x = mat
        m=len(mat)
        n=len(mat[0])
        dp=[[0] * n for _ in range(m)]
        mp = min(m,n)
        g = [[] for _ in range(mp + 1)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    g[dp[i][j]].append((i,j))
        minr = float('inf')
        maxr = float('-inf')
        minc = float('inf')
        maxc = float('-inf')
        for k in range(mp, 0, -1):
            for r,c in g[k]:
                if r<minr : minr = r
                if r>maxr : maxr = r
                if c<minc : minc = c
                if c>maxc : maxc = c
            if maxr - minr >= k or maxc -minc >= k:
                return k*k
        return 0