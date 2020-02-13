#позиционные аргументы

def my_fu(user_name, surname, city, email, phone_num):
    print(user_name, surname, city, email, phone_num)

print('Введите данные пользователя: ')
user_name = str(input('Имя пользователя :'))
surname = str(input('Фамилия :'))
city= str(input('Город проживания :'))
email = str(input('Электронный адрес :'))
phone_num = str(input('Телефон :'))


my_fu(user_name, surname, city, email, phone_num)