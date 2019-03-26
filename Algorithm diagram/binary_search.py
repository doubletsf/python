'''
    二分查找算法 O(logn)
        Author:Double
        Date:2019/3/16
'''
from random import randint

def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low+high)/2) #加int取整，不然报错
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None

#my_list=list(range(1,10))
my_list = [i for i in range(1,10) if randint(0,1)]

print(my_list)
print(binary_search(my_list,3))
print(binary_search(my_list,10))




