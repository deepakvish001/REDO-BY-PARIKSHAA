class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        x = sum(y * z for y, z in zip(prices, discounts))
        return sum(prices) - (x/100.0)
        