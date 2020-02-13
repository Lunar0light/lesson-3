
def int_func(my_str):
    my_list=[]
    for i in my_str:
        my_list = my_list+list(i)
    my_list[0]=(my_list[0]).upper()
    print(*my_list, sep='')

int_func('александр')

