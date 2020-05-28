//通过观察可以发现，如果数组不重复，我们只要找到5的所有倍数的1元素和2元素的集合的排列组合就可得到答案
//但是数组可重复，所以情况太复杂了。算下来的时间复杂度是O(n)
//这里用了前缀和的思路，先在暴力算法的基础上，使用前缀和优化，然后使用哈希表储存，时间复杂度也是O(n)。。。但是比上面简单不是一点半点

#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        unordered_map<int, int> record = {{0, 1}};
        int sum = 0, ans = 0;
        for (int elem: A) {
            sum += elem;
            // 注意 C++ 取模的特殊性，当被除数为负数时取模结果为负数，需要纠正
            int modulus = (sum % K + K) % K;
            if (record.count(modulus)) {
                ans += record[modulus];
            }
            ++record[modulus];
        }
        return ans;
    }
};

int main()
{
    Solution a;
    vector<int>y;
    y.push_back(4);
    y.push_back(5);
    y.push_back(0);
    y.push_back(-3);
    y.push_back(-2);
    y.push_back(1);
    cout<<a.subarraysDivByK(y,5);
    return 0;
}