'''
    此程序为4.3的习题，主要用来练习创建数值列表
                                    Author：Double
                                    Date:2019/3/12
'''

'''
#使用for循环打印数字1-20(含20)
for number in range(1,21):
    print(number)

#创建一个列表，包含数字1-1000000
numbers=list(range(1,1000001))
for number in numbers:
    print(number)

#对1-1000000进行求和
numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#打印1-20的奇数
for number in range(1,21,2):
    print(number)

#打印3-30的3的倍数
for number in range(3,31,3):
    print(number)

#创建立方列表
squares=[]
for number in range(1,1):
    # square=number**3
    # squares.append(square)
    squares.append(number**3)
print(squares)
'''
#立方解析
squares=[number**3 for number in range(1,11)]
print(squares)
print(len(squares))
    

