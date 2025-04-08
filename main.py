import math
from random import *


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
        pizza_0=[f"{pizzas}good smell"]
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

def if_5_8():
    name=['admin','jon','roma','admin Петя','admin Миша']
    for i in name:
        if i in 'admin':
            print( f"здравствуйте,{i},хотите посмотреть отчет о состоянии дел ? \n")
        else:
            print(f"{i},привет,спасибо , что авторизовался в системе \n")
#if_5_8()

def dict_6_1():
    person={'first_name': 'Bill','last_name': 'Gates','age': '69','city': 'Medina',}
    person_1=person.get('town','none \n')
    print(person_1)
    # print(person['first_name'])
    # print(person['last_name'])
    # print(person['age'])
    # print(person['city'])
#dict_6_1()

def dict_6_2():
    name={'Jon':'5','Dan':'10','Adam':'18','Jon_1':'6',}
    for n,a in name.items():
        print(f"\n Name:{n}")
        print(f"Age:{a}")
#dict_6_2()

def trees():
    n1=[]
    n2=[]
    sm=0
    cnt=0
    m=int(input("m="))
    n=int(input("n="))
    for i in range(m):
        t1=randint(25,150)
        n1.append(t1)
    for g in range(n):
        t2=randint(25,150)
        n2.append(t2)
    print("высота деревьев 1 :", n1)
    print("высота деревьев 2 :", n2)
    min_n1=min(n1)
    print("мин.высота деревьев 1:", min_n1)
    min_n2=min(n2)
    print("мин.высота деревьев 2:", min_n2)
    ind_1=n1.index(min_n1)
    print("местоположение меньшего по высоте дерева на 1 дорожке :", ind_1)
    ind_2 = n2.index(min_n2)
    print("местоположение меньшего по высоте дерева на 2 дорожке :", ind_2)
    if ind_1 < ind_2 or ind_1==ind_2:
        for d in range(ind_1+1,len(n1)):
            sm+=n1[d]
            cnt+=1
    else:
        for f in range(ind_2+1,len(n2)):
            sm+=n2[f]
            cnt+=1
    print(cnt)
    cp=round(sm/cnt,1)
    print(cp)
    n1[ind_1]=cp
    n2[ind_2]=cp
    print(n1)
    print(n2)
#trees()

def kr1_1():
    ns=[]
    sn=[]
    ks_1="".join(input("ks="))
    ab=["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ", "ъ","ы", "ь", "э", "ю", "я"]
    print("исходное слово :", ks_1)
    for i in ks_1:
        sp=ab.index(i)
        ns.append(ab[sp+1])
        if len(ks_1)==len(ns):
            ns_1="".join(ns)
            print("зашифрованное слово:",ns_1,'\n')
    for m in ns:
        ps=ab.index(m)
        sn.append(ab[ps-1])
        if len(ns)==len(sn):
            sn_1="".join(sn)
            print("расшифрованное слово:",sn_1)
#kr1_1()

















