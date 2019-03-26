'''
    练习 6-3

'''


vocabulary = {
    'pop': '弹出列表中的元素，默认栈顶',
    'title': '使输出的字符串首字母大写',
    'map': '映射，可代替for循环使数字中每个元素都被作用于指定函数map(f,list)',
    'reduce': '在functoolsba包中，reduce(lambda x,y:x+y,list)',
    'sort': '排序method',
}
for k, v in vocabulary.items():
    print(k + ": " + v + "\n")

# 遍历字典 key+value items():返回key+value
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title()+".")

# 遍历字典中的键 keys():返回key  不加keys()也是默认返回键
for name in favorite_languages.keys():
    print(name.title())

if 'Jen'.lower() not in favorite_languages.keys():
    print("Erin,please take our poll!")

# 遍历字典中的值 values():返回值value
# set()创建不含重复元素的列表
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:") 
for language in set(favorite_languages.values()): 
    print(language.title())
