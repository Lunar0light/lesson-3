
def my_fu(a,b):
    z =  a / b
    print(z)
    return z
print('Введите 2 числа:')
a = float(input())
b = float(input())

try:
    my_fu(a,b)
except ZeroDivisionError:
    print('деление на 0')
