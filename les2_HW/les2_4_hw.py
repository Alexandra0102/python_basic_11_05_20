'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

user_Input = input('Введите строку из нескольких слов, разделенных пробелами \n')
long = len(user_Input)
spaces = [0]

for i in range(long):
    if user_Input[i] == ' ':
        spaces.append(i)
print(spaces)

for space in spaces:
    print(space)

    a = space
    print(user_Input[a:space])



