"""
1)Дан лист:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - найти min число в листе
  - удалить все одинаковые значения
  - заменить каждое четвертое значение на "Х"
  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
пример:
[1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
[-1, -2, 3, 4, 555] => 4
[5, 5, 5, 5] => 5
[-10, 5, 5] => 5

2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
3) переделать первое задание под меню с помощью цикла
4) вывести табличку умножения с помощью цикла while
"""
import math
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# - найти min число в листе
# print(min(list))

#  - удалить все одинаковые значения
# newlist=[]
# for i in list:
#     if i not in newlist:
#         newlist.append(i)
#
# print(newlist)

#  - заменить каждое четвертое значение на "Х"

# for i in range(3,len(list),4):
#         list[i]='x'
# print(list)

'''
- вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
пример:
[1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
[-1, -2, 3, 4, 555] => 4
[5, 5, 5, 5] => 5
[-10, 5, 5] => 5
'''
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2=[-1, -2, 3, 4, 555]
# list3=[5, 5, 5, 5]
# list4=[-10, 5, 5]
#
# def closest(list):
#     newList=[]
#     avg=sum(list)/len(list)
#     for i in range(0,len(list)):
#         newE=math.fabs(list[i]-avg)
#         newList.append(newE)
#         z = newList.index(min(newList))
#     print(list,"=>",list[z])
#
# closest(list4)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# w=int(input("enter width: "))
# h=int(input("enter height: "))
#
# for i in range(h):
#     if i==0 or i==h-1:
#         for j in range(w):
#             print('*',end='')
#     else:
#         print('*',end='')
#         for j in range(1,w):
#             print(' ',end='')
#     print('*',end='')
#     print()

# 3) переделать первое задание под меню с помощью цикла


list = [22, 3,5,2,8,2,-23, 8,23,5]

while True:
    print("list = [22, 3,5,2,8,2,-23, 8,23,5]\n 1 найти min число в листе\n 2 удалить все одинаковые значения\n 3 заменить каждое четвертое значение на Х\n 4 вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа\n 6 Exit")
    task=int(input("Chose task:"))
    if task==1:print(min(list))
    elif task==2:
        newlist = []
        for i in list:
            if i not in newlist:
                newlist.append(i)
        print(newlist)
    elif task==3:
        for i in range(3, len(list), 4):
            list[i] = 'x'
        print(list)
    elif task==4:
        print('list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]\nlist2 = [-1, -2, 3, 4, 555]\nlist3 = [5, 5, 5, 5]\nlist4 = [-10, 5, 5]')
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list2 = [-1, -2, 3, 4, 555]
        list3 = [5, 5, 5, 5]
        list4 = [-10, 5, 5]
        choseList=int(input("Chose list(1,2,3,4):"))
        if choseList==1: listC=list1
        if choseList==2: listC=list2
        if choseList==3: listC=list3
        if choseList==4: listC=list4

        def closest(list):
            newList = []
            avg = sum(list) / len(list)
            for i in range(0, len(list)):
                newE = math.fabs(list[i] - avg)
                newList.append(newE)
                z = newList.index(min(newList))
            print(list, "=>", list[z])
        closest(listC)
    elif task==6:
        break
    else:
        print("Error")
        break
    print("\n______________________________\n")
# 4) вывести табличку умножения с помощью цикла while
# i=1
# j=1
# while i<10:
#     print(i,' ',end='')
#     while j<10:
#         j+=1
#         print(j*i,' ',end='')
#     i+=1
#     j=1
#     print('\n')



