'''
    此程序为3.2的练习题
    1)用列表记录你要请吃饭的人，队列表进行修改


陌生词：1.callable 可调用的
                        Author：Double
                        Date：2019/3/11
'''


name_list=['double','lx','zz']
print("Sincerely invite "+name_list[0]+','+name_list[1]+' and '+name_list[2]+ " to have dinner together")
print(name_list[0]+" can not come to dinner")
name_list[0]='cute girl'
print("Sincerely invite "+name_list[0]+','+name_list[1]+' and '+name_list[2]+ " to have dinner together")
print("I find a bigger table and I want to invite more people have supper")
name_list.insert(0,'sy')
name_list.insert(2,'xx')
name_list.append('laopo')
print("Sincerely invite "+name_list[0]+','+name_list[1]+','+name_list[2]+','+ name_list[3]+ ','+name_list[4]+ ' and '+name_list[5]+ " to have dinner together")
print("I can only invite two friends to have supper")
print("sorry,I can not invite "+name_list.pop()+" to have supper")
print("sorry,I can not invite "+name_list.pop()+" to have supper")
print("sorry,I can not invite "+name_list.pop()+" to have supper")
print("sorry,I can not invite "+name_list.pop()+" to have supper")
print("Sincerely invite "+name_list[0]+' and '+name_list[1]+" to have supper")
print("I invite "+str(len(name_list))+" people to have supper")
del name_list[0]
del name_list[0]
print(name_list)