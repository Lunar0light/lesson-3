
def my_func(x,y):
    c = abs(y)
    a = x
    for i in range(1, c):
        x = 1/(x*a)
    print('result:', x)

x = float(input('введите действительное число :'))
y = int(input('введите целое число:'))
if y > 0:
    y = y * (-1)
my_func(x,y)
