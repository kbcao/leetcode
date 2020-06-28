# 从最后一位开始往前加，每一位考虑有没有来自上一位的进位
# 但其实可以用（位运算），先得到没有考虑进位的结果（a^b）还有进位信息((a&b)<<1)，然后计算两者之和（递归计算）
# 直到进位信息全为0（没有进位）


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        res = ''
        carry = False
        for _ in range(n):
            _sum = int(a[-1])+int(b[-1])+(1 if carry else 0)
            res = str(_sum % 2)+res
            carry = True if _sum >= 2 else False
            a, b = a[:-1], b[:-1]
        return '1'+res if carry else res


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer_without_carry = x ^ y
            carry = (x & y) << 1
            x, y = answer_without_carry, carry
        return bin(x)[2:]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("0", "0"))
