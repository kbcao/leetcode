#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int size = nums.size();
        if (size == 1) {
            return nums[0];
        }
        int first = nums[0], second = max(nums[0], nums[1]);
        for (int i = 2; i < size; i++) {
            int temp = second;
            second = max(first + nums[i], second);
            first = temp;
        }
        return second;
    }
};

int main()
{
  Solution a;
  vector<int>x;
  x.push_back(10);
  x.push_back(1);
  x.push_back(1);
  x.push_back(10);
  cout << a.rob(x);
  return 0;
}