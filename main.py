# Преветствие пользователя
name = input('Добро пожаловать, введите ваше имя:')
print('Приветсвтую,', name)

# Пользователь выбирает операцию
choice = input('''

Выберете опцию:
+ сложение
- вычитание
* умножение
/ деление
''')
num_1 = int(input('Введите первое число: '))   # Ввести первое число
num_2 = int(input('Введите второе число: '))   # Ввесли второе число

# Сложение
if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

# Вычитание
elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

# Умножение
elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)

# Деление
elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

# Ответ
else: print('Enter a valid operator, please run the program again.')

