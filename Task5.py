
def my_func():
    z=0
    for i in range(1, 9999999):
        try:
            my_str = input('Введиче числа через пробел, для суммирования: ', )
            my_str = my_str.split(' ')  # делим через пробел
            my_list = list(my_str)  # преобразуем в список
            my_listt = [float(x) for x in my_list]  #новый список с темиже элементами,но другого типа
            x=sum(my_listt)
            z = z + x
            print(' sum =', z)
        except ValueError:
            my_list = list(my_str)
            my_list.pop() #удалить последний элемент
            my_listt = [float(x) for x in my_list]
            x = sum(my_listt)
            z = z + x
            print(' sum =', z)
            print('end')
            exit()

my_func()









