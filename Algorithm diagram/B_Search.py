'''
调用rotate_Array.py文件中的rotate(nums, k)函数(用来旋转数组)
此程序为旋转数组的二分查找算法
特殊情况:list[low] == list[mid] == list[high]   
        Author:Double
        Date:2019/3/18
'''
#调用单个函数
from rotate_Array import rotate

def B_Search(list, item):
    '''
    :type list: List[int]
    :type item: int  
    '''
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high ) / 2)
        if list[mid] == item:
            return mid
        if list[mid] < list[high]:  #右边有序
            if list[mid] < item and item <= list[high]:
                low = mid + 1
            else:
                high = mid - 1
        elif (list[mid] > list[low]):
            if list[mid] > item and item >= list[low]: #左边有序
                high = mid - 1
            else:
                low = mid + 1
        elif list[mid] == list[high]:   #当数组的左，右，中三个数都相等时，只能逐步缩进，不能折半查找
            high -= 1 
        elif list[mid] == list[low]:
            low += 1
    return None

list=[1,3,5,7,9,10,11]
print("有序数组为: " + str(list))
rotate(list,3)
print("旋转数组为: " + str(list))
print("查找的数字为: 3")
print("查找的数字的位置: " + str(B_Search(list,3)))
        






        



