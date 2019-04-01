''' 
    open()返回一个表示文件的对象，将这个对象存储到后面的使用的变量中
    本例中:文件:pi_digits.txt,变量:file_object

'''

with open('C:/Users/80919/python/practice/chapter_ten/pi_digits.txt') as file_object:
    lines = file_object.readlines()

# lines为列表，文件的每行为列表中的一个元素
pi_string = ''
for line in lines:
    pi_string += line.strip()

# 打印前10位数
print(pi_string[:10] + "...")
print(len(pi_string))
