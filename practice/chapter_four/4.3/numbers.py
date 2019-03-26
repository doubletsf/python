'''
    此程序用来创建数值列表
    1)使用函数range()生成一系列数字
    2)对数字列表执行简单的统计运算 min(),max(),sum()
    3)列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素

                                        Author:Double
                                        Date:2019/3/12

'''

'''
#range()生成数字
for value in range(1,10):
    print(value)
#list()+range()生成数字列表 
numbers=list(range(1,11,2)) #其中2是步长
print(numbers)
'''

'''
#乘方运算
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)

#对数字列表进行统计计算
print(min(range(1,11)))
print(max(range(1,11)))
print(sum(range(1,11)))
'''
#列表解析
squares=[value**2 for value in range(1,11)]
print(squares)


