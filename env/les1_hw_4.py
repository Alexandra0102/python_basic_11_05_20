"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

while True:
    number = input('Введите целое положительное число n \n')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Неверный ввод. Повторите')
max = 0
while number > 0:
    a = number % 10
    if a > max:
        max = a
    number = number // 10
print('Самое большая цифра в числе ' + str(max))

