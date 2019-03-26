'''
    递归sum()对数组求和

'''
from random import randint
from functools import reduce


# 递归函数求和


# def sum(arr):
#     if arr:
#         total = arr.pop()
#         total += sum(arr)
#         return total
#     else:
#         return 0

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

# 使用reduce求和
def sum1(arr):
    return reduce(lambda x, y: x+y, arr)


# 产生随机数组
arr = [i for i in range(0, 11) if randint(0, 1)]

print("输入的数组为: " + str(arr))

# 使用for循环求和
test_total = 0
for i in arr:
    test_total += i


print("for循环求和为: " + str(test_total))
print("递归函数求和为：" + str(sum(arr)))
print("reduce函数求和为: " + str(sum1(arr)))
