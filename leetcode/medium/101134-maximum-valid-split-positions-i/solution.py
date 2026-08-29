import math
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        def get_score(arr):
            m = len(arr)
            if m < 2:
                return 0
            pref = arr[:]
            for i in range(1,m):
                pref[i] = math.gcd(pref[i-1],pref[i])
            suff = arr[:]
            for i in range(m-2, -1,-1):
                suff[i] = math.gcd(suff[i+1],suff[i])
            return sum(pref[i] == suff[i+1] for i in range (m-1))
        vor = nums[:]
        ans = get_score(vor)
        for i in range(len(vor)):
            ans = max(ans,get_score(vor[:i] + vor[i+1:]))
        return ans