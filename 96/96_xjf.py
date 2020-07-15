class Solution:
    def numTrees(self, n: int) -> int:
        mem = [0] * (n + 1)
        mem[0] = mem[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                mem[i] += mem[j] * mem[i - j - 1]
        print(mem)
        return mem[-1]