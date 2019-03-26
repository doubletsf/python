'''
修改、添加和删除元素
    1)列表大多是动态的，意味着列表创建后，将随着程序的运行增删元素
    2)honda为日本本田，ducati为意大利杜卡迪，suzuki为日本铃木
    3)append()可在列表末尾添加元素
    4)insert()可在列表中插入元素
    5)del/pop()/remove()可删除列表中的元素
    6)palette 调色板 'palit

                        Author：Double
                        Date：2019/3/9
'''
motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0]='ducati'
# print(motorcycles)
#在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)
#在列表中插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)
#在列表中删除元素 del方法
del motorcycles[0]
print(motorcycles)
#在列表中删除元素 pop()方法 pop(n)可弹出任何位置，默认栈顶元素
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
#根据值删除元素 remove()方法,但是只能删除第一个指定的值，如果删除的值在列表中
motorcycles.remove('yamaha')
print(motorcycles)
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive.title()+" is too expensive for me.")
