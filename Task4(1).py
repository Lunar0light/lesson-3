def my_func(x,y):
    z = x**y
    print(z)

x = float(input('введите действительное число :'))
y = float(input('введите целое число:'))
if y > 0:
    y = y * (-1)
my_func(x,y)
