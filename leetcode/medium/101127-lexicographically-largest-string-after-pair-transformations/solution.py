class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        cal = nums
        ans = []
        for x in cal:
            z_count = x//(1<<25)
            rem = x % (1<<25)
            res=['z']*z_count
            for i in range(24,-1,-1):
                if(rem >>i) & 1:
                    res.append(chr(ord('a')+i))
            ans.append("".join(res))
        return ans