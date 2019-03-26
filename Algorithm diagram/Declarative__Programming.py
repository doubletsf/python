from functools import reduce
'''
函数式编程：describe what to do, rather than how to do it.
函数式编程的几个技术：
currying：把一个函数的多个参数分解成多个函数， 然后把函数多层封装起来,
    每层函数都返回一个函数去接收下一个参数这样，可以简化函数的多个参数.
map & reduce ：这个技术不用多说了，函数式编程最常见的技术就是对一个集合做Map和Reduce操作。
    这比起过程式的语言来说，在代码上要更容易阅读。
    （传统过程式的语言需要使用for/while循环，然后在各种变量中把数据倒过来倒过去的）这个很像C++中的STL中的foreach，find_if，count_if之流的函数的玩法。


'''

'''
currying
#--------------------------------
def inc(x):
    def incx(y):
        return x + y
    return incx


inc2 = inc(2)
print(inc2(5))
#--------------------------------
'''
'''
# Map
#--------------------------------
def toUpper(item):
    return item.upper()

name = list(map(toUpper, ["tan", "shuang", "feng"]))
print(name)
#--------------------------------
'''

# Map&reduce


def toTitle(item):
    return item.title()


name = list(map(toTitle, ['adam', 'LISA', 'barT']))
print(name)


# def prod(x, y):
#     return x*y


# print(reduce(prod, [1, 3, 5, 7]))

# 求积
def prod():
    return reduce(lambda x, y: x*y, [1, 3, 5, 7])


print(prod())
