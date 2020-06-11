class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st, res = [], [0] * len(T)
        for i in range(len(T)):
            while st and (T[i] > T[st[-1]]):
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return res