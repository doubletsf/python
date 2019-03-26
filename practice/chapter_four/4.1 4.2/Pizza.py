'''
    此程序为4.2的习题，主要用来练习for循环操作

                                    Author:Double
                                    Date:2019/3/12

'''
#Pizzas
print("Pizzas:")
Pizzas=['new york stytle','chicago style','pan pizza']
'''
for Pizza in Pizzas:
    print("\nI like "+Pizza.title()+" pizza!")
print("I really love pizza!")
#animals
print("animals:")
animals=['cat','dog','pig']
for animal in animals:
    print("\nA "+animal+" would make a great pet")
print("Any of these animals would make a great pet!")
'''
friends_pizzas=Pizzas[:]
#print(friends_pizzas)
Pizzas.append('double pizza')
friends_pizzas.append('xx pizza')
# print(Pizzas)
# print("\n"+str(friends_pizzas))
for Pizza in Pizzas[:]:
    print(Pizza)

