'''
    选择排序算法 O(n^2)
    randint(0,1)随机产生0或者1
    random.randint() produces a random integer in the range specified, boundaries include
        Author：Double
        Date:2019/3/16
'''

from random import randint

# 查找列表中最大元素
def FindBiggest(arr):
    index=0
    biggest=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>biggest:
            biggest=arr[i]
            index=i
    return index

# 选择排序算法
def SelectionSort(arr):
    sortarr=[]
    for i in range(len(arr)):
        biggest=FindBiggest(arr)
        sortarr.append(arr.pop(biggest))
    return sortarr
    
arr=[i for i in range(1,20) if randint(0,1)]
# print(randint(0,2))，测试randint()功能

# 输出未排序的列表
print(arr)
# 输出python自带的sorted排序方法
# print(sorted(arr,reverse=True))
arr.sort(reverse=True)
print(arr)
#输出排序后的列表，从大到小排序
print(SelectionSort(arr))






