def my_func(args):
    if a > b and a > c and (b != c):
        max1 = a
        max2=max(b,c)
        sum1 = max1 + max2
    elif b > a and b > c and (a != c):
        max1 = b
        max2 = max(a, c)
        sum1 = max1 + max2
    elif c > a and c > b and (a != b):
        max1 = c
        max2 = max(a, b)
        sum1 = max1 + max2
    elif a == b and a > c:
        sum1=a+b
    elif a == b and a < c:
        sum1='наибольшее число только одно'
    elif a == c and a > b:
        sum1 = a + c
    elif a == c and a < b:
        sum1='наибольшее число только одно'
    elif b == c and b > a:
        sum1 = b + c
    elif b == c and b < a:
        sum1='наибольшее число только одно'
    elif b == c and a == c:
        print('Числа равны, сумма двух: ')
        sum1 = b + c
    print(sum1)

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
args = [a, b, c]
my_func(args)
