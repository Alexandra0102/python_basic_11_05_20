'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''



user_Input = input('Введите строку из нескольких слов, разделенных пробелами \n')
long = len(user_Input)
spaces = [0]
for i in range(long):
    if user_Input[i] == ' ':
        spaces.append(i)

a = 0
j = 0
for space in spaces:
    if j != 0:
        if len(user_Input[a:space]) > 10:
            print(f'слово номер {j}: ' + user_Input[a:a+10])
        else:
            print(f'слово номер {j}: ' + user_Input[a:space])
    a = space
    j += 1
if len(user_Input[a:len(user_Input)]) > 10:
    print(f'слово номер {j}: ' + user_Input[a:a + 10])
else:
    print(f'слово номер {j}: ' + user_Input[a:len(user_Input)])


