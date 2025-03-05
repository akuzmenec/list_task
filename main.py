import math

def task_3_1():
    names=['jon','dania']
    print(names[0])
    print(names[-1])

def task3_2():
    names = ['jon', 'dania']
    massage= f"hello {names[0]}"
    print(massage)

def task3_5():
    names = ['jon', 'dania']
    del names[0]
    print(names)

def task_3_6():
    names = ['jon', 'dania',"Alex"]
    names.insert(0, 'Dan')
    names.insert(2, 'Artem')
    names.append('Sergey')
    print(names)

def task_3_7():
    names = ['Dan', 'jon', 'Artem', 'dania', 'Alex', 'Sergey']
    names.pop(0)
    names.pop(1)
    names.pop(2)
    names.pop(-1)
    print(names)

def task_4_1():
    pizzas="pepperoni","three cheeses","mushroom"
    for pizza in pizzas:
        pizza_0=[f"{pizzas()}good smell"]
        print(pizza_0)
def t():
    for i in range(100+1):
        print(i)


def t4_3():
    for numbers in range(1,20+1):
        print(numbers)
def t4_4():
    numbers= list(range(1,1000000+1))
    print(sum(numbers),"-sum")
    print(min(numbers),"-min")
    print(max(numbers),"-max")
def t4_6():
    numbers = list(range(1,20+1,2))
    print(numbers,"нечетные числа")

def t4_10():
    list=['apple','banana','broomstick','orange','tangerine']
    print("первые 3 пункта в списке - это :")
    for i in list [0:3]:
        print(i.title())
    print("\nтри пункта из середины списка:")
    for a in list [1:4]:
        print(a)
    print("\nпоследние 3 пункта в списке - это")
    for b in list[-3:]:
        print(b)

#t4_10()
def tg4_10():
    list = ['apple', 'banana', 'broomstick', 'orange','tangerine']
    list_1=[ i for i in list[0:3]]
    print(list_1)
    print("\nтри пункта из середины списка:")
    list_2=[a for a in list[1:4]]
    print(list_2)
    print("\nпоследние 3 пункта в списке - это")
    list_3=[b for b in list [-3:]]
    print(list_3)
#tg4_10()
def t4_11():
    pizza = ['pepperoni', 'three cheeses']
    friend_pizza = pizza[:]
    friend_pizza.append('pineapple pizza')
    pizza.append('mushroom')
    print(friend_pizza,pizza)
#t4_11()
def t4_13():
    tuples=(1,2,3,)
    print('original:')
    for tuple in tuples:
        print(tuple)
    print('\nmodified:')
    tuples=(9,2,3,)
    for motuples in tuples:
        print(motuples)
#t4_13()

def t5_1():

    car='bmw'
    print("Is car=='bmw'? I predict True.")
    print(car=='bmw')

    print("\nIs car =='bmw'? I predict False.")
    print(car=='audi')

def i_f5_3():
    alien_color=['green','yellow','red']
    if 'green' in alien_color:
        print('+5')
    if 'black' in alien_color:
        print()

def i_f5_4():
    alien_color = ['green', 'yellow', 'red']
    if 'green' in alien_color:
        print('+5')
    else:
        print(+10)












