class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        return s[::-1] == s
