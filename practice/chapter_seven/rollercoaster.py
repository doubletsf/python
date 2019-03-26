'''
input()练习，相当于C的scanf()
7-2 to 7-3
'''
# message = input("请问要租赁什么样的汽车:\n")
# print("Let me see if i can find you a " + message + ".")

# 7-2
# message = input("How many people are there to eat:\n")
# message = int(message)
# if message > 8:
#     print("There is no empty table.")
# else:
#     print("There is an empty table.")

# 7-3 判断输入数字是否是10的整数倍
# message = input("please input a number:\n")
# message = int(message)
# if message % 10 == 0:
#     print("It is an integer multiple of 10. ")
# else:
#     print("It is not an integer multiple of 10.")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"  
message = "" 
while message != 'quit':   
    message = input(prompt)         
    if message != 'quit':      
        print("\n" + message)  