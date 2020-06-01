# easy


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max=max(candies)
        return [True if i-_max+extraCandies >=0 else False for i in candies]
        