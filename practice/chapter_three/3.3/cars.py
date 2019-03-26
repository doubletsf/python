'''
    此程序用来练习对列表进行排序操作
    1)sort()方法可以对列表进行永久性排序
    2)sorted()对列表进行临时排序
    3)reverse()方法可以反转列表元素

陌生单词：1.toyota 丰田 2.subaru 斯巴鲁

                                        Author:Double
                                        Date:2019/3/12
'''
cars=['bmw','audi','toyota','subaru']

'''
#sort()方法
cars.sort() 
print(cars)
#按字母表反向排序
cars.sort(reverse=True) 
print(cars)
#sorted()方法
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
'''
print(cars)
cars.reverse()
print(cars)
print(len(cars))

