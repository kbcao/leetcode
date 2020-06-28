# 和三数之和类似，只不过改一改target
# 先排序，然后选一个作为一个第一个数，后面两个数的选取用双端指针，往中间靠

class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        close=target+100000000
        for i in range(len(nums)-2):
            t=target-nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                if (abs(nums[l]+nums[r]+nums[i]-target)<abs(target-close)):
                    close=nums[l]+nums[r]+nums[i]
                if nums[l]+nums[r]>t:
                    r-=1
                elif nums[l]+nums[r]<t:
                    l+=1
                else:
                    return target
        return close

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([0,1,2],3))
