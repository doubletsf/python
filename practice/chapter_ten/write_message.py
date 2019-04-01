'''
    读取模式('r')、写入模式('w')、附加模式('a')
'''

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("Double love programming.\n")
    file_object.write("XX love programming.\n")