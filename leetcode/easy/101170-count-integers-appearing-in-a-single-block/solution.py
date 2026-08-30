class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        a = set()
        b = set()
        prev = -1
        for x in nums:
            if x in a and x != prev:
                b.add(x)
            a.add(x)
            prev = x
        return len(a) - len(b)
        