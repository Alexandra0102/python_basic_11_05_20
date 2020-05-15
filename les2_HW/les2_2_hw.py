'''2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''

numbers = []
while True:
    userInput_2 = input('Введите количество элементов индекса \n')
    if userInput_2.isdigit():
        userInput_2 = int(userInput_2)
        break
    else:
        print('Неверный ввод. Повторите')
for i in range(userInput_2):
    while True:
        userInput = input('Введите элементы индекса \n')
        if userInput.isdigit():
            userInput = int(userInput)
            break
        else:
            print('Неверный ввод. Повторите')
    numbers.append(userInput)
print(numbers)
if userInput_2 % 2 != 0:
    a = userInput_2 - 2
else:
    a = userInput_2

for i in range(a):
    if i % 2 == 0:
        k = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = k
print(numbers)


