'''
此程序为5.4的练习题

'''
#-------------------------------
# 5-8 to 5-9
# users=['double','xx','zz','xxx','admin']
# if users:
#     for user in users:
#         if user == 'admin':
#             print("Hello admin,would you like to see a status report?")
#         else:
#             print("Hell " + str(user) + ",thank you for logging in again.")
# else:
#     print("We need to find some users!")

# 5-10
# current_users = ['Double','Xx','zz','xxx','admin','lx','xxxx']

# #将列表中的元素变成小写
# current_users = [item.lower() for item in current_users]
# print(current_users)
#-------------------------------

#-------------------------------
# new_users = ['double','XX','sb','sx','sd']

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print("This user has been used,please input other username.")
#     else:
#         print("This user hasn't been used.")
#-------------------------------

#-------------------------------
# 5-11
list = [ num for num in range(1,10)]

print(list)
# for num in list:
for i in range(0,len(list)):
    if i == 0 :
        print(str(list[i]) + ":1st")
    elif i == 1:
        print(str(list[i]) + ":2nd")
    elif i == 2:
        print(str(list[i]) + ":3rd")
    else:
        print(str(list[i]) + ":"+str(i) + "st")
        

