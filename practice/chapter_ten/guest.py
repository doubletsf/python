'''
    提示用户输入名字，添加名字到guest.txt中

'''
filename = 'guest.txt'

with open(filename, 'a') as file_object:
    while(1):
        user_names = input("Please input your name:\n")
        print("Hello," + user_names)
        file_object.write(user_names + "\n")
        out =input("please input 'q' to quit.\n")
        if out == 'q':
            break
   
        
        