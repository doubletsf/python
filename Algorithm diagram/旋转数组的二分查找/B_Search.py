import sys
sys.path.insert(0, 'C:/Users/80919/python/Algorithm diagram')
from rotate_Array import rotate
'''
调用rotate_Array.py文件中的rotate(nums, k)函数(用来旋转数组)
此程序为旋转数组的二分查找算法
特殊情况:list[low] == list[mid] == list[high]
调用不同目录下其他文件的函数:
    import sys
    sys.path.append('D:/')
    import B
    if __name__=="__main__":
    print B.pr(x,y)
        Author:Double
        Date:2019/3/18
'''
# 调用单个函数



def B_Search(list, item):
    '''
    :type list: List[int]
    :type item: int  
    '''
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        if list[mid] == item:
            return mid
        if list[mid] < list[high]:  # 右边有序
            if list[mid] < item and item <= list[high]:
                low = mid + 1
            else:
                high = mid - 1
        elif (list[mid] > list[low]):
            if list[mid] > item and item >= list[low]:  # 左边有序
                high = mid - 1
            else:
                low = mid + 1
        elif list[mid] == list[high]:  # 当数组的左，右，中三个数都相等时，只能逐步缩进，不能折半查找
            high -= 1
        elif list[mid] == list[low]:
            low += 1
    return None


list = [1, 2, 5, 7, 9]
print(list)
rotate(list, 1)
print(str(list)+"\n"+str(B_Search(list, 7)))
