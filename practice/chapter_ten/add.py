'''
    10-6 to 10-7

'''


def add(num1, num2):
    '''
    :type num1: int
    :type num2: int
    :rtype: int
    '''
    sum = num1 + num2
    return sum


print("Please input 2 numbers:")
while(1):
    try:
        num1 = int(input())
        num2 = int(input())
    except ValueError:
        print("please input number")
    else:
        print("The sum of the two is: " + str(add(num1, num2)))
        break
