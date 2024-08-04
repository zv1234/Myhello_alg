

#选择排序
def search_sort(lists):
    #剩下的为最大元素
    for index in range(len(lists)-1):
        j=index
        #每次从为排序的后面选择最大的
        for i in range(index+1,len(lists)):
            if lists[j]>lists[i]:
                j=i
        lists[index],lists[j]=lists[j],lists[index]
    return lists

#冒泡排序
def bubble_sort(nums: list[int]):
    n = len(nums)
    # 外循环：未排序区间为 [0, i]
    for i in range(n - 1, 0, -1):
    # 内循环：将未排序区间 [0, i] 中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

#插入排序

def insert_sort(nums):
    # 我们在未排序区间选择一个基准元素，将该元素与其左侧已排序区间的元素逐一比较大小，并将
    # 该元素插入到正确的位置。
    for i in range(1,len(nums)):
        j=i-1
        base=nums[i]
        while j>=0 and nums[j]>base:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=base
    return nums
#二分查找
def binary_search(nums: list[int], target: int) -> int:
    # 初始化双闭区间 [0, n-1] ，即 i, j 分别指向数组首元素、尾元素
    i, j = 0, len(nums) - 1
    # 循环，当搜索区间为空时跳出（当 i > j 时为空）
    while i <= j:
    # 理论上 Python 的数字可以无限大（取决于内存大小），无须考虑大数越界问题
        m = (i + j) // 2 # 计算中点索引 m
        if nums[m] < target:
            i = m + 1 # 此情况说明 target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1 # 此情况说明 target 在区间 [i, m-1] 中
        else:
            return m # 找到目标元素，返回其索引
    return -1 # 未找到目标元素，返回 -1
#二分查找查找左右边界
#查找
#左右边界
#局部最小


#异或 相同为0，不同为1 无进位相加
#0^n=n n^n=0

if __name__ == '__main__':
    a=[1,4,2,2,5,3]
    print(insert_sort(a))

