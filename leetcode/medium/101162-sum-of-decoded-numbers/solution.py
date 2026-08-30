class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        a = nums
        t = 0
        MOD = 10**9 + 7
        for num in a:
            w = num %10
            d = num // 10

            s = str(d)
            x = int(s[:w])
            y = int(s[w:])

            t = (t + pow(x,y,MOD)) % MOD
        return t