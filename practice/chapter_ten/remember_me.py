'''
    代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。
    这样的过程被称为重构。
    重构让代码更清晰、更易于理解、更容易扩展

'''

import json


filename = "username.json"
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?\n")
    with open(filename, 'w') as f_boj:
        json.dump(username, f_obj)
        print("We'll remeber you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
