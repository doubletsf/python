'''
    此程序用来练习操作字符串
    使用到的快捷键：
    1）三个\'''进行多行注释或者选中多行使用Ctrl+/
    陌生单词：1）indent 缩进
                                            Author：Double
                                            Date：2019/3/9
'''
name="double"
print("\n\t\"Hello "+name.title()+",would you like to learn some Python today?\"")
lover_name="lx"
'''
    print("\n\t"+lover_name.lower())将字符串全部转换成小写
    print("\n\t"+lover_name.upper())将字符串全部转换成大写
    print("\n\t"+lover_name.title())将字符串的首字母全部换成大写
'''
famous_person="double"
message=" once said,\"The night is dark and full of terrors.\" "
    #print(name+" once said,\"The night is dark and full of terrors.\"")
print("\t"+famous_person+message.lstrip()+'a') #lstrip()消除开头的空白
print("\t"+famous_person+message.rstrip()+'a') #rstrip()消除末尾的空白
print("\t"+famous_person+message.strip()+'a')  #strip()消除字符串两端空白 
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)
print(str(5+3)+"\n"+str(9-1)+"\n"+str(2*4)+"\n"+str(16/2))
favorite_num=2
print("My favorite number is "+str(favorite_num))