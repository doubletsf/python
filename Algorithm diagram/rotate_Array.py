'''
旋转数组
Example 1:
    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
其中注释：
    type:    Type of a parameter.
    vartype: Type of a variable. 
    rtype:   Return type. 

'''
#空间复杂度为O(n)的解法
# def rotate_Array(arr,k):

#空间复杂度为O(1)的解法
def rotate(nums, k):
    '''
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything,modify nums in-place instead
    '''
    l = len(nums)
    k = k%l
    nums[:] = nums[l-k:] + nums[:l-k] #反转数组，使用切片

# nums = [1,2,3,4,5,6,7]
# print(nums)
# rotate(nums,3)
# print(nums)



