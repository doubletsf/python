import json


def store_user_number():
    '''获取用户喜欢的数字'''
    filename = 'number.json'
    try:
        with open(filename) as f_obj:
            user_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_number


def get_user_number():
    '''提示用户输入新的数字'''
    filename = 'number.json'
    try:
        with open(filename, 'w') as f_obj:
            user_number = input("Please input your favorite number:\n")
            json.dump(user_number, f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_number


def read_user_number():
    ''' 读取用户最喜欢的数字'''
    user_number = store_user_number()
    if user_number:
        print("I know your favorite number! It's " + user_number)
    else:
        user_number = get_user_number()
        print("I'll remeber your favoriter number" + user_number + "!")

read_user_number()
