# 重点在于：当a的长度确定之后，b的长度也会确定（当然a和b对应的串也就确定了），所以只需要遍历a的长度，则可以直接完成匹配
# 细节：1. 保证要枚举的字母（e.g. a）出现至少一次，因此如果b比a多，就把ab对调
#      2. 边界情况处理
#      3. 只有a没有b


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        # 统计 a 和 b 的出现次数，并让 a 是较多的一个
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        # 边界情况
        if not value:
            return count_b == 0
        if not pattern:
            return False

        # 遍历a匹配的字符串的长度
        for len_a in range(len(value) // count_a + 1):
            # 去除a匹配的之后，还剩下多少可以给b匹配
            rest = len(value) - count_a * len_a
            #  没有b，只有a                      留给b的字符串长度可以被每个b平分
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos+len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos+len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                # 如果a为当前长度时，遍历完整个pattern串后完全匹配了，则说明当前a的长度和b的长度都是合理的，匹配成功了，直接返回
                if correct and value_a != value_b:
                    return True
        # 所有a的长度都试过了，都没法匹配，返回False
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.patternMatching("abba","dogcatcatdog"))

