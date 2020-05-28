class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        n = 0
        res = ''
        while i < len(s):
            c = s[i]
            i += 1
            if c.isalpha(): res += c
            elif c.isdigit(): n = n * 10 + int(c)
            elif c == '[':
                old_i = i
                cnt = 1
                while cnt > 0:
                    if s[i] == '[': cnt += 1
                    elif s[i] == ']': cnt -= 1
                    i += 1
                res += n * self.decodeString(s[old_i:i - 1])
                n = 0
        return res