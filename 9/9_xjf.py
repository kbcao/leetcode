class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0): return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            if x == y: return True
            x //= 10
        return x == y
