class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        of = False
        res = ''
        for i in range(max(len(a), len(b))):
            na = '0' if i >= len(a) else a[i]
            nb = '0' if i >= len(b) else b[i]
            if na == '0' and nb == '0':
                res += '1' if of else '0'
                of = False
            elif na == '1' and nb == '1':
                res += '1' if of else '0'
                of = True
            else:
                res += '0' if of else '1'
        if of: res += '1'
        return res[::-1]