import json

# 将数据保存为json格式
'''
numbers = [1, 2, 3, 4]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
'''

# 从json文件中读取数据
filename = 'numbers.json'
with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
