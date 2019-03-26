'''
    递归查找列表中最大的数字
    random.shuffle()洗乱列表中元素的顺序 shuffle 洗
    用Python自带的max()方法验证

    调试问题:
        Python默认的递归深度为1000，可以通过sys.getrecursionlimit()查看
        可以通过sys.setrecursionlimit()修改
        巧用切片list[1:],每次可切掉第一个元素
        Author:Double
        Date:2019/3/17
'''
from random import randint
import random
import sys


def findBiggest(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = findBiggest(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


sys.setrecursionlimit(10000)
arr = [i for i in range(0, 20) if randint(0, 1)]
random.shuffle(arr)

print(arr)
print(max(arr))
print(findBiggest(arr))
