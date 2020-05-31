class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 该代码通过。但是用dict不太好，因为后面的keys遍历会使得
        # 复杂度从理论上的O(n)变为O(n^2)，最理想是用栈。
        # heights.append(0)
        # cur = {}
        # cur_h = 0
        # res = 0
        # for i in range(len(heights)):
        #     h = heights[i]
        #     if h > cur_h: cur[h] = i
        #     elif h == cur_h: pass
        #     else:
        #         if h not in cur: cur[h] = i
        #         for key in list(cur.keys()):
        #             if key > h:
        #                 res = max(res, key * (i - cur[key]))
        #                 cur[h] = min(cur[h], cur[key])
        #                 del cur[key]
        #     cur_h = h
        # return res

        # 根据题解优化后的用栈的版本
        heights.append(0)
        st = [(0, 0)]
        res = 0
        for i in range(len(heights)):
            h = heights[i]
            if h > st[-1][0]: st.append((h, i))
            else:
                i_l = i
                while st[-1][0] > h:
                    res = max(res, (i - st[-1][1]) * st[-1][0])
                    i_l = st[-1][1]
                    st.pop()
                if st[-1][0] < h: st.append((h,i_l))
        return res