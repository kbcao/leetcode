# 第k大指的是 升序排列后的倒数第k个元素
# 1. 排序后取-k个元素
# 2. 建立一个小顶堆，里面最多就只有k个元素，那么第一个就是答案，每次放进去的时候都replace第一个，然后往下downShift
#    如果当前元素比第一个元素还小，则直接扔掉，因为其肯定比第k大要小
# 3. 快速排序，每次第k个元素到位，判断是不是要的第K个，否则往左或者往右搜索

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        small_heap=[]
        # 最小堆放入k个
        for i in range(k):
            heapq.heappush(small_heap,nums[i])
        
        # 最小堆的顶就是答案（第k个大值），因此如果比这个值大，则替换掉这个，然后让他down，比这个值小就直接不考虑了
        for i in range(k,len(nums)):
            if nums[i]>small_heap[0]:
                heapq.heapreplace(small_heap,nums[i])
        return small_heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(nums,l,r):
            pivot=l
            i=l
            j=r
            while i<j:
                while i<j and nums[j]>nums[pivot]:
                    j-=1
                while i<j and nums[i]<=nums[pivot]:
                    i+=1
                nums[i],nums[j]=nums[j],nums[i]
            nums[j],nums[pivot]=nums[pivot],nums[j]
            if j==len(nums)-k:
                return nums[j]
            elif j>len(nums)-k:
                return quick(nums,l,j-1)
            else:
                return quick(nums,j+1,r)
        return quick(nums,0,len(nums)-1)

