"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

while True:
    number = input('Введите число n от 1 до 10 \n')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Неверный ввод, повторите, пожалуйста')

if (1 <= number) and (number <= 9):
    summa = number * 1 + number * 11 + number * 111
    print(summa)
else:
    print('Неверное число, повторите, пожалуйста')


