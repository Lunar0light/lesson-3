
name= 'Деление'
def my_fu(name, *args):

    z =  args[1] / args[2]
    print(z)
    return z
print('Введите 2 числа:')  #через enter
args = input()

try:
    my_fu(name, *args)
except ZeroDivisionError:
    print('деление на 0')
