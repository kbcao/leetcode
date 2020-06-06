# 没做出来
# 第一种方法是把所有值放在set里面，然后遍历每一种可能的开头，然后去set里面一直搜下一个

# 还有一种方法是建立dict，某个值 to 包含其的连续序列的长度 的映射
# 每次看一个值，看 值-1 和 值+1 的长度，总长度就是 他们的和+1
# 然后要更新左边和右边的长度，但是不用都更新，更新左顶点和右顶点就ok

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num2length=dict()
        max_len=0
        for num in nums:
            if num not in num2length:
                left=num2length.get(num-1,0)
                right=num2length.get(num+1,0)
                cur_length=left+right+1
                max_len=max(max_len,cur_length)
                num2length[num]=cur_length
                # 只需要更新端点的值，因为下次也只会碰到端点
                num2length[num-left]=cur_length
                num2length[num+right]=cur_length
        return max_len

