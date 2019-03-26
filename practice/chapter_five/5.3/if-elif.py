'''
    此程序用来测试if-elif语句

'''
age=64

if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5

print("Your admission cost is $"+str(price)+".")