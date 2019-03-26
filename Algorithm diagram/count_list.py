'''
    递归函数计算列表中包含的元素数

'''
from random import randint

#定义全局变量count用于计数
global count
count=0

#递归函数
def count_list(arr):
    global count
    if arr:
        count+=1
        arr.pop()
        count_list(arr)
        return count
    else:
        return 0

#创建列表
arr=[i for i in range(0,20) if randint(0,1)]

#输出列表
print(arr)
#用python自带的len()方法来计算列表包含的元素数
print(len(arr))
#用自己写的递归函数来计算列表包含的元素数目
print(count_list(arr))

        