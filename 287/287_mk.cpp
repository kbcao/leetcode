class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size();
        int x[n-1];
        int re;
        for(int i=0;i<n-1;++i){
            x[i]=0;
        }
        for(int i=0;i<n;++i){
            x[nums[i]-1]++;
        }
        for(int i=0;i<n-1;++i){
            if(x[i]>1) re=i+1;
        }
        return re;
    }
};