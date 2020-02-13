def int_func(my_str):
    my_list=[]
    for i in my_str:
        my_list = my_list+list(i)
    my_list[0]=my_list[0].upper()
    print(*my_list, sep='')
                                        #my_str.lstrip(' ', ' ' ')
                                        #не выходит удалить литеры из строки, чтобы присвоить переменную
                                        #и выводить в 1 строку
new_str=input('Введите строку: ')
new_list = new_str.split(' ')
my_len=len(new_list)
for o in range(my_len):
    int_func(new_list[o])
